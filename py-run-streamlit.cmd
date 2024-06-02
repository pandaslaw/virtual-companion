@echo off

call ./install-requirements.cmd

streamlit run ./src/run_streamlit.py
