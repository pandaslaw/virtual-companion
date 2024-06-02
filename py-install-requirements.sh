#!/bin/sh

python3 -m venv ./venv
source ./venv/bin/activate

python -m pip install --upgrade pip
pip install -r requirements.txt

chmod +x ./py-run-bot.sh && chmod +x ./py-run-server.sh && chmod +x ./py-run-streamlit.sh