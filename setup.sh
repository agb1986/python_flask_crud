echo 'Creating venv'
python -m venv ./.env;

echo 'Starting venv'
source ./.env/Scripts/activate;

echo 'Pulling dependencies'
pip install -r requirements.txt;

echo 'Starting Flask server'
flask run | pytest tests/test.py;
