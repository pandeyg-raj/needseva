#!/bin/bash
python3 -m venv venv/
source venv/bin/activate
pip install -r requirements.txt
export FLASK_APP=application.py
export FLASK_DEBUG=1
python3 sqldatabase.py
