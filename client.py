# echo-client.py

import socket

HOST = "127.0.0.1"  # The server's IP address
PORT = 65432  # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    username = input("Please enter your user name: ")
    password = input("Please enter your password: ")
    login_params = username + password
    s.sendall(login_params.encode())
    data = s.recv(1024)

print(data.decode())
