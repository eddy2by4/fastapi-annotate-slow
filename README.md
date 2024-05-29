Setup:
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

Start server:
fastapi dev main.py

wrk -t12 -c300 -d15s http://localhost:8000/
Running 15s test @ http://localhost:8000/
  12 threads and 300 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency    13.51ms   28.07ms 648.17ms   98.77%
    Req/Sec     2.26k   198.33     3.34k    78.61%
  406104 requests in 15.04s, 48.41MB read
  Socket errors: connect 0, read 465, write 0, timeout 0
Requests/sec:  27008.01
Transfer/sec:      3.22MB


wrk -t12 -c300 -d15s http://localhost:8000/slow
Running 15s test @ http://localhost:8000/slow
  12 threads and 300 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency    32.03ms   80.36ms   1.23s    97.62%
    Req/Sec     1.15k   117.65     1.74k    71.67%
  206276 requests in 15.07s, 24.59MB read
  Socket errors: connect 0, read 771, write 0, timeout 0
Requests/sec:  13684.37
Transfer/sec:      1.63MB


