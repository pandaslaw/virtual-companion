@echo off

call ./py-install-requirements.cmd

python -m uvicorn main:app --port 5000
