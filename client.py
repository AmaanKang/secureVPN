import socket

def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client_socket.connect(("127.0.0.1",12345))
        print(f"Connected to server at 127.0.0.1:12345")
        # TODO Authentication: Send an authentication token or credentials
        # For now, we'll just send a test message to the server
        client_socket.send(b"Hello from client!")
        response = client_socket.recv(1024)
        print(f"Received from server: {response.decode('utf-8')}")
    except Exception as e:
        print(f"Error connecting to server: {e}")
    finally:
        client_socket.close()

if __name__ == "__main__":
    main()

