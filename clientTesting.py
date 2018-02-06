import socket

TCP_IP = '192.168.0.1'
TCP_PORT = 5005
BUFFER_SIZE = 1024
MESSAGE = "Hello, World!"

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect((TCP_IP, TCP_PORT))

message = "test"
while message is not "quit":
    message = input("Message to send: ")
    clientSocket.send(message)
    data = clientSocket.recv(BUFFER_SIZE)

clientSocket.close()