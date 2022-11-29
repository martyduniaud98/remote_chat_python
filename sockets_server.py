# SOCKETS NETWORK : SERVER

import socket

HOST_IP = "<IP_serveur>"
HOST_PORT = 22222
MAX_DATA_SIZE = 1024

s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((HOST_IP, HOST_PORT))
s.listen()

print("Waiting for connection on address : ",
      HOST_IP, "port", HOST_PORT, "...")
connection_socket, client_adress = s.accept()
print("Connection established with : ", client_adress)

while True:
    text_send = input("you: ")
    connection_socket.sendall(text_send.encode())
    data_received = connection_socket.recv(MAX_DATA_SIZE)
    print("Message : ", data_received.decode())


s.close()
connection_socket.close()
