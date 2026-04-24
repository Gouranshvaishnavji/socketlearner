import socket
import threading

nickname = input("WHo are you? _")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 55555)) #server is on 55555 too

def receive():
    """Listens for messages from the server."""
    while True:
        try:
            # Receive Message From Server
            # If 'NICK' Send Nickname
            message = client.recv(1024).decode('ascii')
            if message == 'NICK':
                client.send(nickname.encode('ascii'))
            else:
                print(message)
        except Exception:
            # Close Connection When Error
            print("error")
            client.close()
            break

def write():
    """mocking the client message sending architecture iwth this template function."""
    while True:
        message = f'{nickname}: {input("")}'
        client.send(message.encode('ascii'))

receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()