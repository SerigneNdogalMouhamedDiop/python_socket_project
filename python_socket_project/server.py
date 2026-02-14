import socket

host = "127.0.0.1"
port = 5000

s = socket.socket()
s.bind((host, port))
s.listen(1)

print("Serveur en attente...")
conn, addr = s.accept()
print("Client connecté :", addr)

message = "Bienvenue sur le serveur"
conn.send(message.encode())

conn.close()

print ("Bonjfffffour")
