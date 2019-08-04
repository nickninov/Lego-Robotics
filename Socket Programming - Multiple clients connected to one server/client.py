import socket

# Create a socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the remote host and port
sock.connect(('localhost', 8888))

while True:

    message = input("Enter a message: ")

    # Send a request to the host
    sock.send(message.encode())

# Terminate
sock.close()

