import socket
import threading

HOST = "127.0.0.1"
PORT = 5000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

print("Chat server started.")
print("Waiting for a client to connect...")

client, address = server.accept()

print("Client connected:", address)
print("You can start chatting!")
print("Type 'exit' to stop the chat.\n")


def receive_messages():
    while True:
        try:
            message = client.recv(1024).decode()

            if not message or message.lower() == "exit":
                print("\nClient disconnected.")
                break

            print(f"\nClient: {message}")
            print("You: ", end="", flush=True)

        except:
            break


thread = threading.Thread(target=receive_messages)
thread.daemon = True
thread.start()
while True:
    message = input("You: ")

    if message.lower() == "exit":
        client.send("exit".encode())
        break

    client.send(message.encode())

client.close()
server.close()
print("Chat ended.")
