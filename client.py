import socket
import sys

def start_client(port):
    server_ip = "127.0.0.1" # formal ip for local host
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    try:
        # Message to send
        message = "Hello, World!"
        
        # Send data
        client_socket.sendto(message.encode(), (server_ip, port))
        print(f"[+] Data send: {message}")

        # Receive response
        data, server = client_socket.recvfrom(1024)
        print(f"[+] Data recv: {data.decode()}")
        print(f"[*] Server address: {server}")

    except Exception as e:
        print(f"[!] Error: {e}")
    finally:
        client_socket.close()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python client.py <port>")
    else:
        start_client(int(sys.argv[1]))