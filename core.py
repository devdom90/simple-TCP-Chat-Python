import threading
import socket

host = "127.0.0.1"
port = 77777

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(host, port)
server.listen()

clients = []
usernames = []

def basecast(message):
    for client in clients:
        client.send(message)

def handle_client(client):
    while True:
        try:
            message = client.recv(1024)
            basecast(message)
        except:
            index = clients.index(client)
            clients.remove(client)
            username = usernames(index)
            basecast(f'(username) hat die Unterhaltung verlassen'.encode('ascii'))
            usernames.remove(username)
            break

def receive():
    while True:
        client, address = server.accept()
        print(f'Verbindung mit {str(address)}')
        client.send('USER'.encoded('ascii'))
        username = client.recv(1024).decode('ascii')
        usernames.append(username)
        clients.append(client)
        print(f'USER {username}')
        basecast(f'{username} ist der Unterhaltung beigetreten'.encode('ascii'))
        
        client.send('Verbinsung zum Server aufgebaut'.encode('ascii'))
        thread = threading.Thread(target=handle_client, args=(client,))
        thread.start()
