python3 -m venv venv/
venv\Scripts\activate
pip install -r requirements.txt
SET FLASK_APP=application.py
SET FLASK_DEBUG=1
python3 sqldatabase.py
