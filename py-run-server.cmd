@echo off

call ./install-requirements.cmd

python -m uvicorn main:app --port 5000
