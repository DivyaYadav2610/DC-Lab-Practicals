import socket
import threading


def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode("utf-8")
            if not message:
                break
            print("\n" + message)
        except OSError:
            break


def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(("127.0.0.1", 12345))
    threading.Thread(target=receive_messages,
                     args=(client_socket,), daemon=True).start()

    print("Connected. Type messages; type 'exit' to quit.")
    try:
        while True:
            message = input()
            if message.lower() == "exit":
                break
            client_socket.sendall(message.encode("utf-8"))
    finally:
        client_socket.close()


if __name__ == "__main__":
    main()
