#!/bin/bash
export PYTHONPYCACHEPREFIX="$(dirname "$0")/.cache/pycache"
python3 "$(dirname "$0")/main.py"
