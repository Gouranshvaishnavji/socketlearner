import socket
import threading # as we have lots of users on smae instance making multiple processes, we need to use threads to handle multiple clients at the same time

host = '127.0.0.1'
port = 55555

#using ipv4 and tcp server we specify AF_INET and SOCK_STREAM
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

# Lists For Clients and Their Nicknames
clients = []
nicknames = []

def broadcast(message):
    for client in clients:
        client.send(message)

def handle(client):
    while True:
        try:
            message = client.recv(1024) # message for client in 1024 but buffer, we are waiting for it to send us something
            broadcast(message)
        except: 
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            print(f'{nickname} disconnected.')
            broadcast(f'{nickname} left the chat!'.encode('ascii'))
            nicknames.remove(nickname)
            break
            raise

def receive():
    print(f"Server is listening on {host}:{port}...")
    while True:
        client, address = server.accept()
        print(f"connected with {str(address)}")

        client.send('NICK'.encode('ascii'))
        nickname = client.recv(1024).decode('ascii')
        nicknames.append(nickname)
        clients.append(client)
        print(f"Nickname is {nickname}")
        broadcast(f"{nickname} joined the chat!".encode('ascii'))
        client.send('connected to server!'.encode('ascii'))

        thread = threading.Thread(target=handle, args=(client,)) # client we got from server.accept() is passed to handle function as argument
        thread.start()

receive()