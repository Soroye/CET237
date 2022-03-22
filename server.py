# echo-server.py

import socket
import math, random

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)

def generate_one_time_password():
    # container for all digits
    DIGITS = "0123456789"
    OTP = ""
 
   
    # creating the digits in the generator
    for i in range(6) :
        OTP += DIGITS[math.floor(random.random() * 10)]
    #encoding the digits as sendall accepts only binary data
    return ("Your OTP is " + OTP).encode()

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print(f"Connected by {addr}") #Testing connection
        while True:
            data = conn.recv(1024)
            if not data:
                break
            login_paramms = data.decode()
            login_paramms = str(login_paramms)
            if login_paramms == "dare1234":
                conn.sendall(generate_one_time_password())
            else:
                conn.sendall(b"Incoorrect username or password")
