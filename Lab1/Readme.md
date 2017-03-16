Requirements:
Question from https://github.com/sithu/cmpe273-spring17/tree/master/lab1

Use psutil and implement a network socket monitoring tool that can check how many TCP sockets are being created by a web application.

Create a Python script called socket-mon.py.

List all processes that have any socket connections (meaning the laddr and raddr fields exist).Group by the PID and sort the output by the number of the connections per process.Expected Output in CSV format

$ python socket-mon.py (or $ sudo python socket-mon.py)

"pid","laddr","raddr","status"

"1234","10.0.0.1@48776","93.186.135.91@80","ESTABLISHED"

"1234","10.0.0.1@48777","93.186.135.91@80","ESTABLISHED"

"5678","10.0.0.1@48779","193.286.35.91@8000","CLOSING"



