@echo off

source ./install-requirements

python -m uvicorn main:app --port 5000