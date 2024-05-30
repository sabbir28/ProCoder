import socket

# Constants
HOST = '127.0.0.1'
PORT = 65432
BUFFER_SIZE = 1024

def login(username, password):
    """
    Send login request to the server.

    Parameters:
    username (str): The user's username.
    password (str): The user's password.

    Returns:
    str: The server's response.
    """
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall(f"{username},{password}".encode('utf-8'))
        response = s.recv(BUFFER_SIZE).decode('utf-8')
        return response

if __name__ == "__main__":
    username = input("Enter username: ")
    password = input("Enter password: ")

    response = login(username, password)
    print(response)
