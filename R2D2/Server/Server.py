from Weather import getWeather
import socket
import os

server = socket.socket()

# Bind the socket
server.bind(('192.168.1.68', 4200))

server.listen(1)

print("Server is running")

while True:
    clientConnection, address = server.accept()

    print("Connected with address "+ str(address[0]))

    clientConnection.send(bytes("You just connected with "+ address[0], 'utf-8'))

    while True:
        message = clientConnection.recv(1024).decode()
        print("Client said: "+message+"\n")

        # Stop server
        if message.lower() == "quit" or message.lower() == "":
            print("Closing server")
            clientConnection.send(bytes("quit", 'utf-8'))
            clientConnection.close()
            server.close()
            os._exit(0)

        # Check weather
        elif message.lower() == "weather":
            # Get weather value
            message = getWeather()

            # Check if function has failed
            if message == "Failed":
                clientConnection.send(bytes("Failed", 'utf-8'))
            else:
                clientConnection.send(bytes(message, 'utf-8'))

        # Return ok message
        # else:
        #     clientConnection.send(bytes("ok", 'utf-8'))

    clientConnection.close()

server.close()