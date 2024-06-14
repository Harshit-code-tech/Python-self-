import socket
import threading

# Server configuration
HOST = '127.0.0.1'  # Localhost
PORT = 55555

# List to store client connections
clients = []


# Function to handle client connections
def handle_client(client_socket):
    while True:
        try:
            # Receive message from client
            message = client_socket.recv(1024).decode('utf-8')
            if not message:
                # If no message received, client has disconnected
                print("Client disconnected")
                clients.remove(client_socket)
                client_socket.close()
                break

            # Broadcast message to all connected clients
            print(f"Received message: {message}")
            broadcast(message, client_socket)
        except:
            # If any error occurs, close the client connection
            clients.remove(client_socket)
            client_socket.close()
            break


# Function to broadcast message to all clients except sender
def broadcast(message, sender):
    for client in clients:
        if client != sender:
            try:
                client.send(message.encode('utf-8'))
            except:
                # If unable to send message, close the client connection
                client.close()
                clients.remove(client)


# Main function to start the server
def main():
    # Create server socket
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind server socket to host and port
    server.bind((HOST, PORT))

    # Listen for incoming connections
    server.listen()

    print("Server is listening...")

    while True:
        # Accept incoming connection
        client_socket, addr = server.accept()
        print(f"Connected with {addr}")

        # Add client socket to list of clients
        clients.append(client_socket)

        # Create a new thread to handle client connection
        client_thread = threading.Thread(target=handle_client, args=(client_socket,))
        client_thread.start()


if __name__ == "__main__":
    main()
