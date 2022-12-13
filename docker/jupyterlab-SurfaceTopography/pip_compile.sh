#!/bin/bash
#
# regenerate requirements.txt
#
python3 -m venv venv
source venv/bin/activate

pip install --upgrade pip
pip install wheel
pip install pip-tools

pip-compile requirements.in > requirements.txt
