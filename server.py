import socket
import threading

def handle_client(client_socket):
    try:
        while True:
            request = client_socket.recv(1024)
            if not request:
                break
            else:
                client_socket.send(request)
    except Exception as e:
        print(f"Error handling client: {e}")
    finally:
        client_socket.close()

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("0.0.0.0",12345))
    server_socket.listen(1)

    print("Server is listening on port 12345....")

    while True:
        client_socket,client_address = server_socket.accept()
        print(f"Connection from {client_address}")
        client_handler = threading.Thread(target=handle_client,args=(client_socket,))
        client_handler.start()

if __name__ == "__main__":
    main()