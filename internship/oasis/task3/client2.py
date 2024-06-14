import socket
import threading
import time
# Server configuration
HOST = '127.0.0.1'  # Localhost
PORT = 55555


# Function to receive messages from server
def receive_messages(client_socket):
    while True:
        try:
            # Receive message from server
            message = client_socket.recv(1024).decode('utf-8')
            print(message)
        except:
            # If any error occurs, close the client connection
            print("Connection closed by server")
            client_socket.close()
            break


# Main function to start the client
def main():
    # Create client socket
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect to server
    client.connect((HOST, PORT))

    # Start a thread to receive messages from server
    receive_thread = threading.Thread(target=receive_messages, args=(client,))
    receive_thread.start()

    # Send messages to server
    while True:
        message = input()
        client.send(message.encode('utf-8'))
        time.sleep(1)


if __name__ == "__main__":
    main()
