import streamlit as st
from langchain_community.llms import Ollama
from langchain_core.prompts import ChatPromptTemplate

from src.companion import Companion
from src.config import app_settings

CHARACTER_TO_PROMPT_MAPPING = {
    Companion.ROMANTIC: app_settings.PROMPT_FOR_ROMANTIC_CONVERSATION,
    Companion.FRIENDLY: app_settings.PROMPT_FOR_FRIENDLY_CONVERSATION,
}


def generate_response(input_text: str, companion_character: Companion):
    prompt = CHARACTER_TO_PROMPT_MAPPING.get(companion_character)
    if not prompt:
        st.warning("Please check prompts mapping!", icon="⚠")

    full_prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                f"{prompt}. Please respond to the questions and requests very kindly.",
            ),
            ("user", "Query:{question}"),
        ]
    )
    llm = Ollama(model="llama2")

    # Create a chain that combines the prompt and the Ollama model
    chain = full_prompt | llm

    if input_text:
        st.write(chain.invoke({"question": input_text}))
