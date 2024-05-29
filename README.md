python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

wrk -t12 -c300 -d15s http://localhost:8000/
wrk -t12 -c300 -d15s http://localhost:8000/slow


