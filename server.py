import socket
import threading
import hashlib
from cryptography.fernet import Fernet
import base64

# This is a test secret key.
# TODO Improve the authentication and encryption in this file.
with open('keys/serverKey.txt','rb') as file:
    SECRET_KEY = file.read()

fernet = Fernet(base64.urlsafe_b64encode(SECRET_KEY))

def handle_client(client_socket):
    try:
        # Receive the authentication token from the client
        token = client_socket.recv(1024)
        # Check if the token matches the hashed secret key
        if hashlib.sha256(token).digest() != hashlib.sha256(SECRET_KEY).digest():
            print("Authentication failed")
            return
        print("Authentication successful")

        while True:
            request = client_socket.recv(1024)
            if not request:
                break
            else:
                # Decrypt the request
                decrypted_request = fernet.decrypt(request)
                print(f"Received: {decrypted_request.decode('utf8')}")

                # Encrypt the response
                response = fernet.encrypt(b"Hello from server!")
                client_socket.send(response)
    except Exception as e:
        print(f"Error handling client: {e}")
    finally:
        client_socket.close()

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("0.0.0.0",1194))
    server_socket.listen(5)

    print("Server is listening on port 1194....")

    while True:
        client_socket,client_address = server_socket.accept()
        print(f"Connection from {client_address}")
        client_handler = threading.Thread(target=handle_client,args=(client_socket,))
        client_handler.start()

if __name__ == "__main__":
    main()