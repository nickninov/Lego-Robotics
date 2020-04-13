from Battery import Battery
from TouchSensor import Button
from Actions import Actions
from datetime import datetime
import socket

if __name__ == '__main__':

    try:
        # Create client socket
        client = socket.socket()

        # Connect to server
        client.connect(('192.168.1.68', 4200))

        message = client.recv(1024).decode()
        print("Server message: " + message)

        # Starting battery thread
        battery = Battery(client)

        # Starting button thread
        button = Button(client)

        # Declare movement
        action = Actions()

        print("Start main thread\n")

        while True:
            action.movement(client)

    # Server is not connected
    except ConnectionRefusedError:
        # Get current time HH:MM:SS
        now = datetime.now()
        time = now.strftime("%H:%M:%S")
        print(str(time) + ": Server is not connected")