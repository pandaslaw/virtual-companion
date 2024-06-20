import telebot
from loguru import logger

from src.companion import Companion
from src.config import app_settings
from src.utils import generate_answer, generate_answer_stable_diffusion

bot_guru = telebot.TeleBot(app_settings.TELEGRAM_BOT_GURU_TOKEN)


@bot_guru.message_handler(commands=['start', 'hello'])
def send_welcome_guru(message):
    logger.info("Starting a conversation...")
    greeting_text = "Hola, que paso?👋😉"
    sent_msg = bot_guru.send_message(message.chat.id, greeting_text)
    bot_guru.register_next_step_handler(sent_msg, send_message_guru)


def send_message_guru(message):
    companion_character = Companion.GURU
    user_text = message.text
    answer_message = generate_answer_stable_diffusion(user_text, companion_character=companion_character)
    sent_msg = bot_guru.send_message(message.chat.id, answer_message)
    bot_guru.register_next_step_handler(sent_msg, send_message_guru)


if __name__ == '__main__':
    logger.info("Telegram bot-guru is live.")
    bot_guru.infinity_polling()
