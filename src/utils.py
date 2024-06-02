import streamlit as st
from langchain_community.llms import Ollama
from langchain_core.prompts import ChatPromptTemplate
from loguru import logger
import datetime as dt

from src.companion import Companion
from src.config import app_settings

CHARACTER_TO_PROMPT_MAPPING = {
    Companion.ROMANTIC: app_settings.PROMPT_FOR_ROMANTIC_CONVERSATION,
    Companion.FRIENDLY: app_settings.PROMPT_FOR_FRIENDLY_CONVERSATION,
}


def generate_answer(input_text: str, companion_character: Companion):
    if not input_text:
        raise ValueError("Your message is empty.")

    system_prompt = CHARACTER_TO_PROMPT_MAPPING.get(companion_character)
    if not system_prompt:
        raise ValueError(f"There is no corresponding prompt for companion type {companion_character.value}")

    full_prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                f"{system_prompt}. Please respond to the questions and requests very kindly.",
            ),
            ("user", "Query:{question}"),
        ]
    )
    llm = Ollama(model="llama2")

    # Create a chain that combines the prompt and the Ollama model
    chain = full_prompt | llm

    logger.info("Generating an answer...")
    start_time = dt.datetime.now()
    output = chain.invoke({"question": input_text})
    running_secs = (dt.datetime.now() - start_time).microseconds
    logger.info(f"Answer generation took {running_secs/100000:.2f} seconds.")

    return output


def write_response_to_streamlit(input_text: str, companion_character: Companion):
    output = generate_answer(input_text, companion_character)
    st.write(output)
