import socket

import threading



HOST = '127.0.0.1'

PORT = 5500



server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((HOST, PORT))



clients = []

usernames = {}





def handle_client(client):

    while True:

        try:

            message = client.recv(1024).decode('utf-8')

            for c in clients:

                if c != client:  

                    c.send(message.encode('utf-8'))

        except:

            index = clients.index(client)

            clients.remove(client)

            client.close()

            break





def receive():

    server.listen()

    print("Server is listening...")

    while True:

        client, address = server.accept()

        print(f"Connected with {address}")



        client.send("Welcome to ChatApp!".encode('utf-8'))

        username = client.recv(1024).decode('utf-8')

        usernames[client] = username



        clients.append(client)



        thread = threading.Thread(target=handle_client, args=(client,))

        thread.start()





receive()

