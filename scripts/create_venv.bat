cd ..
python -m venv venv
.\venv\Scripts\activate
pip freeze > requirements.txt
pip install -r requirements.txt
.\venv\Scripts\deactivate