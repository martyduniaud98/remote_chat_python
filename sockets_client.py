import socket
import time

HOST_IP = "<IP_SERVER>"
HOST_PORT = 22222
MAX_DATA_SIZE = 1024

s = socket.socket()

print("Connection to the server : ", HOST_IP, "port", HOST_PORT)
while True:
    try:
        s.connect((HOST_IP, HOST_PORT))
    except ConnectionRefusedError:
        print("ERROR: Unable to connect to server. Reconnect......")
        time.sleep(5)
    else:
        print("Connected to server.")
        break

while True:
    data_received = s.recv(MAX_DATA_SIZE)
    print("Message : ", data_received.decode())
    text_send = input("vous: ")
    s.sendall(text_send.encode())

s.close()
