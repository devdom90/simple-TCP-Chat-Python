import threading
import socket



base = "127.0.0.1"

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(base, 77777)

def get_content():
    while True:
        try:
            message = client.recv(1024).decode('ascii')
            if message == "USER":
                pass
            else:
                print(message)
        except:
            print("Etwas ist schief gelaufen")