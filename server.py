import socket

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("0.0.0.0",12345))
    server_socket.listen(1)

    print("Server is listening on port 12345....")

    while True:
        client_socket,client_address = server_socket.accept()
        print(f"Connection from {client_address}")

if __name__ == "__main__":
    main()