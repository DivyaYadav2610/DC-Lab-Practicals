import socket
import threading

clients = []
clients_lock = threading.Lock()


def broadcast(message, sender):
    with clients_lock:
        current_clients = list(clients)
    for client in current_clients:
        if client != sender:
            try:
                client.sendall(message.encode("utf-8"))
            except OSError:
                pass


def handle_client(client_socket, address):
    print(f"Client {address} connected.")
    try:
        while True:
            message = client_socket.recv(1024).decode("utf-8")
            if not message:
                break
            print("Received:", message)
            broadcast(message, client_socket)
    except OSError:
        pass
    finally:
        with clients_lock:
            if client_socket in clients:
                clients.remove(client_socket)
        client_socket.close()
        print(f"Client {address} disconnected.")


def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind(("0.0.0.0", 12345))
    server.listen(5)
    print("Server started. Waiting for clients...")

    while True:
        client_socket, address = server.accept()
        with clients_lock:
            clients.append(client_socket)
        threading.Thread(target=handle_client,
                         args=(client_socket, address), daemon=True).start()


if __name__ == "__main__":
    main()
