@echo off

source ./install-requirements.sh

python -m uvicorn main:app --port 5000