import datetime as dt
import json

import requests
import streamlit as st
from langchain_community.llms import Ollama
from langchain_core.prompts import ChatPromptTemplate
from loguru import logger

from src.companion import Companion
from src.config import app_settings

CHARACTER_TO_PROMPT_MAPPING = {
    Companion.GURU: app_settings.PROMPT_FOR_GURU_CONVERSATION,
    Companion.ROMANTIC: app_settings.PROMPT_FOR_ROMANTIC_CONVERSATION,
    Companion.DEV: app_settings.PROMPT_FOR_DEV,
}


def generate_answer(input_text: str, companion_character: Companion):
    if not input_text:
        return "? what do you mean"

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
    logger.info(f"Answer generation took {running_secs / 100000:.2f} seconds.")

    return output


def generate_answer_stable_diffusion(input_text: str, companion_character: Companion):
    if not input_text:
        return "? what do you mean"

    system_prompt = CHARACTER_TO_PROMPT_MAPPING.get(companion_character)
    if not system_prompt:
        raise ValueError(f"There is no corresponding prompt for companion type {companion_character.value}")

    url = "https://stablediffusionapi.com/api/v5/uncensored_chat"
    payload = json.dumps({
        "key": app_settings.STABLE_DIFFUSION_API_KEY,
        "messages": [
            {
                "role": "assistant",
                "content": system_prompt
            },
            {
                "role": "user",
                "content": input_text
            },
        ],
        "max_tokens": 1000
    })

    headers = {
        'Content-Type': 'application/json'
    }

    logger.info("Guru: Generating an answer...")
    start_time = dt.datetime.now()

    response = requests.request("POST", url, headers=headers, data=payload)
    content = json.loads(response.content)
    output = content.get("message")

    running_secs = (dt.datetime.now() - start_time).microseconds
    logger.info(f"Guru: Answer generation took {running_secs / 100000:.2f} seconds.")

    return output


def write_response_to_streamlit(input_text: str, companion_character: Companion):
    output = generate_answer(input_text, companion_character)
    st.write(output)
