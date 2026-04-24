import socket
import sys

def start_server(port):
    # Create a UDP socket (SOCK_DGRAM)
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    try:
        server_socket.bind(('0.0.0.0', port)) # we use 0.0.0.0 as this is a wildcard address that allows the server to listen on all available network interfaces. This is useful for servers that need to accept connections from any IP address, rather than being limited to a specific one.
        print(f"[*] Server listening on port {port}...")

        while True:
            # Receive message and client address
            data, addr = server_socket.recvfrom(1024)
            message = data.decode()
            print(f"[+] Data recv: {message}")

            # Send acknowledgment back to the specific client address
            response = "Welcome to the UDP Server."
            server_socket.sendto(response.encode(), addr)
            print(f"[+] Data send: {response}")

    except Exception as e:
        print(f"[!] Error: {e}")
    finally:
        server_socket.close()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python server.py <port>")
    else:
        start_server(int(sys.argv[1]))