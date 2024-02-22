
for unit test
```
python -m unittest -q "File_Name" | Out-Null 
```


# Secure Chat Application

## Introduction:
This project aims to develop a real-time secure chat application from scratch, resembling popular messaging apps like WhatsApp and Signal, with a focus on end-to-end encryption. The key components covered in this project include:
-	Socket Programming
-	Real-Time System 
-	End-to-end Encryption(E) 

## Features and Functionalities:
The secure chat application provides the following features:
-	Multi-User group chat application
-	Encryption modes:
    -	Two keys (RSA, EL GAMAL) 
-	TTP (Third Trusted Party) facilitating interactions between two parties who both trust the third party

## Technology Stack:
-	Python as the server-side language
-	Tkinter library for UI
-	Socket library for real-time message exchange

## System Design Overview:
The system functionality can be summarized in simple steps:
- User registration
- User login
- Admin login and server startup
- Admin can manage user(i.e add, delete USer)
- User can initiate chats
- Server starts at the HOST IPv4 at the chosen PORT
- Client attempts to connect to the server 
- Server accepts the client connection
- Server generates a session key for the accepted client
- Client sends a username to the server
- Client and server start a listener thread
- User sends a message (after encryption using one of the encryption modes)
- Server sends the cipher to all clients, including the sender
- Client receives the cipher and starts decryption
- Server continues to receive messages from other clients
- Server keeps listening for any new client connections
- Server is responsible for sending and receiving messages containing information like username, message, and required keys

## System Overview:
![System Overview](https://github.com/bishal78441/securechatapplication/blob/main/project_overview.png)

## Installation
Open terminal and type the following command
```
git clone https://github.com/bishal78441/securechatapplication
```

### Usage
Start by running the start up script
```
python start_up.py
```

## System Output:
![GUI](https://github.com/bishal78441/securechatapplication/blob/main/GUI.png)

for unit test
```
python -m unittest -q "File_Name" | Out-Null 
```
