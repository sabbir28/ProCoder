import socket
import threading

# Constants
HOST = '127.0.0.1'
PORT = 65432
MAX_LOGIN_ATTEMPTS = 5
BUFFER_SIZE = 1024

# Dummy data for demonstration
users_db = {
    'john_doe': 'password123',
    'jane_doe': 'securepassword'
}

def verify_login(username, password):
    """
    Verify the user's credentials.

    Parameters:
    username (str): The user's username.
    password (str): The user's password.

    Returns:
    bool: True if the credentials are correct, False otherwise.
    """
    return users_db.get(username) == password

def handle_client(conn, addr):
    """
    Handle client connections.

    Parameters:
    conn (socket): The client connection.
    addr (tuple): The client address.
    """
    print(f"Connected by {addr}")
    try:
        data = conn.recv(BUFFER_SIZE).decode('utf-8')
        if data:
            username, password = data.split(',')
            if verify_login(username, password):
                response = 'Login successful'
            else:
                response = 'Invalid credentials'
            conn.sendall(response.encode('utf-8'))
    finally:
        conn.close()

def main():
    """
    Main function to start the server.
    """
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        print(f"Server listening on {HOST}:{PORT}")

        while True:
            conn, addr = s.accept()
            threading.Thread(target=handle_client, args=(conn, addr)).start()

if __name__ == "__main__":
    main()
