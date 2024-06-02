from dotenv import load_dotenv
from loguru import logger
from pydantic.v1 import BaseSettings


class AppSettings(BaseSettings):
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

    APP_TITLE: str

    OPENAI_API_KEY: str
    HUGGINGFACEHUB_API_TOKEN: str
    PROMPT_FOR_FRIENDLY_CONVERSATION: str
    PROMPT_FOR_ROMANTIC_CONVERSATION: str
    TELEGRAM_BOT_TOKEN: str


logger.info("Loading environment variables from .env file.")
load_dotenv()
app_settings = AppSettings()
