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
    STABLE_DIFFUSION_API_KEY: str

    PROMPT_FOR_GURU_CONVERSATION: str
    PROMPT_FOR_ROMANTIC_CONVERSATION: str
    PROMPT_FOR_DEV: str

    TELEGRAM_BOT_GURU_TOKEN: str
    TELEGRAM_BOT_TOKEN: str
    TELEGRAM_BOT_DEV_TOKEN: str


logger.info("Loading environment variables from .env file.")
load_dotenv()
app_settings = AppSettings()
