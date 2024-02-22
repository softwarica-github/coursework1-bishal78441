import socket
import threading
import secrets
from tkinter import E
import el_gamal
import RSA
import atexit
import datetime


HOST = '192.168.1.68'
PORT = 99
LISTENER_LIMIT = 5
active_clients = []  # List of all currently connected users
flagmethod = "1"

# Function to listen for upcoming messages from a client
def listen_for_messages(client, username, key, elgamapublickey, rsa_string):

    while 1:

        message = client.recv(2048).decode('utf-8')
        print("RECV : ",message)
        if message != '':
            ####### send
            final_msg = username + '~' + message + '~' + key + "~" + flagmethod + "~" + elgamapublickey + "~" + rsa_string
            send_messages_to_all(final_msg)
            print("Message:   ",final_msg)

        else:
            print(f"The message send from client {username} is empty")


# Function to send message to a single client
def send_message_to_client(client, message):

    client.sendall(message.encode())
    print("SEND : ", message.encode() )

# Function to send any new message to all the clients that
# are currently connected to this server
def send_messages_to_all(message):

    for user in active_clients:

        # Start the security phase using message then pass the message to client
        send_message_to_client(user[1], message)

# Function to handle client
def client_handler(client, key):
    # Server will listen for client message that will
    # Contain the username
    while 1:
        username = client.recv(2048).decode('utf-8')
        print("RECV : ", username)
        if username != '':
            active_clients.append((username, client, key))
            # generate session key
            key = secrets.token_hex(8).upper()

            # RSA parameters
            n, E, D = RSA.calc()
            print("public and private key parameters:")
            print("n: ", n)
            print("E: ", E)
            print("D: ", D)
            print("\n")

            rsa_string = ""
            rsa_string += str(n)
            rsa_string += ","
            rsa_string += str(E)
            rsa_string += ","
            rsa_string += str(D)
            rsa_string += ","

            # ElGamal public key
            string_ints = [str(x) for x in ElgamalKey]
            elgamalpublickey = ",".join(string_ints)
            print("elgamal public key", elgamalpublickey)

            # Send prompt message
            prompt_message = "SERVER~" + f"{username} added to the chat~" + key + "~" + flagmethod + "~" + elgamalpublickey + "~" + rsa_string
            send_messages_to_all(prompt_message)

            print("Session key successfully generated for " + f"{username } ==>", key)

            break
        else:
            print("Client username is empty")

    threading.Thread(target=listen_for_messages, args=(client, username, key, elgamalpublickey, rsa_string,)).start()


# Main function
def main():
    global ElgamalKey
    ElgamalKey = el_gamal.generate_public_key()
    # Creating the socket class object
    # AF_INET: we are going to use IPv4 addresses
    # SOCK_STREAM: we are using TCP packets for communication
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Creating a try-except block
    try:
        server.bind((HOST, PORT))
        print(f"Running the server on {HOST}:{PORT}")
        server.listen(LISTENER_LIMIT)

        # This while loop will keep listening to client connections
        while 1:
            client, address = server.accept()
            print(f"Successfully connected to client {address[0]} {address[1]}")
            key = ""
            threading.Thread(target=client_handler, args=(client, key,)).start()

    except OSError as e:
        print(f"Unable to bind/listen: {e}")
        # Handle the error gracefully, close the socket if created
        if server:
            server.close()


log_file = "chat_log.txt"  # Define the log file name

# Function to save chat messages to a log file with timestamp
def save_chat_log(message):
    timestamp = datetime.datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")
    with open(log_file, "a") as file:
        file.write(f"{timestamp} {message}\n")  # Append the message with timestamp to the log file

def send_messages_to_all(message):
    for user in active_clients:
        send_message_to_client(user[1], message)
        save_chat_log(message)  # Save the message to the log file

def save_chat_on_exit():
    # Save chat log when the server terminates
    with open(log_file, "a") as file:
        file.write(f"{datetime.datetime.now().strftime('[%Y-%m-%d %H:%M:%S]')} === Chat Ended ===\n")

# Register the function to be called on program exit
atexit.register(save_chat_on_exit)

if __name__ == "__main__":
    main()