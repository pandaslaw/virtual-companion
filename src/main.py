from fastapi import FastAPI
from loguru import logger

from src.companion import Companion
from src.config import app_settings
from src.user_message import UserMessage
from src.utils import generate_answer

app = FastAPI(
    title=app_settings.APP_TITLE if app_settings.APP_TITLE else "Virtual Companion API service",
    responses={404: {"description": "not found"}},
)


@app.get("/")
async def root():
    """Returns the content for the start page and a response code."""

    return "Welcome to Virtual Companion app!"


@app.post("/send-message")
def process_user_message(user_message: UserMessage):
    """Posts user's message to AI model and returns its response."""

    logger.info("Starting to process user's message..")
    companion_character = Companion.ROMANTIC
    prediction = generate_answer(user_message.text, companion_character)
    result = {"prediction": prediction}
    return result
