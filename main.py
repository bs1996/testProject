import socket
import json
# initializing socket
s = socket.socket()
host = '192.168.0.166'
port = 12345

# binding port and host
s.bind((host, port))

# waiting for a client to connect
s.listen(5)

while True:
    # accept connection
    c, addr = s.accept()
    print('got connection from addr', addr)
    data = '{"x": "100, "y" : "200"}'
    d = json.loads(data)

    # sending data type should be string and encode before sending
    c.send(d.encode())
    c.close()