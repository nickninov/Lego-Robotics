from socket import *
import sys
from _thread import *

# Sets host and port to accept data
host = ''
port = 8888

# Creates socket
s= socket(AF_INET, SOCK_STREAM)

print("Socket created!")

try:
# Binds the Server socket to a specific IP address + Port number
    s.bind((host, port))
    print("Socket bound!")
except error:
# Will catch any errors that might prevent the binding
    print("Binding failed!")
    sys.exit()

# Socket listens for requests. Currently listening for 10 request at a time
s.listen(10)


def clientthread(conn):

    while True:
        data = conn.recv(1024)
        reply = "Data: "+data.decode()

        if not data:
            break;

        print(reply)
        conn.sendall(data)
        print()

    conn.close()

print("Socket is ready!")


while True:

    # Create a socket for specific client
    conn, addr = s.accept()
    print("Connected with %s: %s" % (addr[0], str(addr[1])))

    # Opens a new thread for a client
    start_new_thread(clientthread, (conn,))

s.close();

