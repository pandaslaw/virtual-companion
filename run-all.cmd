@echo off

python -m venv venv
call venv\Scripts\activate.bat

pip install -r requirements.txt

set PYTHONPATH=%PYTHONPATH%;.\src

streamlit run ./src/run_streamlit.py
