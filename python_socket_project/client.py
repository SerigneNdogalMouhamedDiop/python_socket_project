import socket

host = "127.0.0.1"
port = 5000

s = socket.socket()
s.connect((host, port))

message = s.recv(1024).decode()
print("Message du serveur :", message)

s.close()

print("Test Git commit")
print("Bonjour")
