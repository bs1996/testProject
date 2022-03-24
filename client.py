import socket
import json
s = socket.socket()
host = '192.168.0.166'
port = 12345

# connect to host
s.connect((host, port))

# recv message and decode here 1024 is buffer size.
print(s.recv(1024).decode())
s.close()