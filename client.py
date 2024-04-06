import socket
import hashlib
from cryptography.fernet import Fernet
import base64

# This is a test secret key.
# TODO Improve the authentication and encryption in this file.
with open('keys/clientKey.txt','rb') as file:
    SECRET_KEY = file.read()

fernet = Fernet(base64.urlsafe_b64encode(SECRET_KEY))

# ISSUE - Import Connection is failing on OpenVPN.
# openssl req -new -nodes -out client.csr -config client.cnf
# openssl x509 -req -in client.csr -CA root.crt -CAkey root.key -CAcreateserial -out client.crt -days 365 -extensions v3_req -extfile client.cnf
def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client_socket.connect(("127.0.0.1",1194))
        print(f"Connected to server at 127.0.0.1:1194")

        # Send the secret key as an authentication token
        client_socket.send(SECRET_KEY)

        # Encrypt the message
        message = fernet.encrypt(b"Hello from client!")
        client_socket.send(message)

        response = client_socket.recv(1024)

        # Decrypt the response
        decrypted_response = fernet.decrypt(response)
        print(f"Received from server: {decrypted_response.decode('utf-8')}")
    except Exception as e:
        print(f"Error connecting to server: {e}")
    finally:
        client_socket.close()

if __name__ == "__main__":
    main()

