@echo off

call ./py-install-requirements.cmd

streamlit run ./src/run_streamlit.py
