import socket
import threading

HOST = "127.0.0.1"
PORT = 5000

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

print("Connected to the chat server!")
print("Type 'exit' to leave the chat.\n")


def receive_messages():
    while True:
        try:
            message = client.recv(1024).decode()

            if not message or message.lower() == "exit":
                print("\nServer disconnected.")
                break

            print(f"\nServer: {message}")
            print("You: ", end="", flush=True)

        except:
            break


thread = threading.Thread(target=receive_messages)
thread.daemon = True
thread.start()

while True:
    message = input("You: ")

    if message.lower() == "exit":
        break

    client.send(message.encode())

client.close()
print("Chat ended.")
