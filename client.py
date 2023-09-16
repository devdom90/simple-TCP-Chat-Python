import threading
import socket

username = input("Wähle einen Benutzername...")

base = "127.0.0.1"

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(base, 77777)

def get_content():
    while True:
        try:
            message = client.recv(1024).decode('ascii')
            if message == "USER":
                client.send(username.encode('ascii'))
                pass
            else:
                print(message)
        except:
            print("Etwas ist schief gelaufen")
            client.close()
            break



def create_content():
    while True:
        message = f'{username} sagt: {input("")}'
        client.send(message.encode('ascii'))



get_thread = threading.Thread(target=get_content)
get_thread.start()
post_thread = threading.Thread(target=create_content)
post_thread.start()

    
