#!/bin/sh

source ./py-install-requirements.sh

python -m uvicorn main:app --port 5000