from Battery import Battery
from TouchSensor import Button
from Actions import Actions
from RobotDisplay import RobotDisplay
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

        # Start Ev3 screen
        display = RobotDisplay('maker')
        display.startScreen()

        # Starting battery thread
        battery = Battery(client, display)

        # Starting button thread
        button = Button(client, display)

        # Declare movement
        action = Actions()

        print("Start main thread\n")

        while True:
            action.movement(client, display)

    # Server is not connected
    except ConnectionRefusedError:
        # Declare movement
        action = Actions()

        # Play error sound
        action.playFile("Sounds/4.wav")

        # Get current time HH:MM:SS
        now = datetime.now()
        time = now.strftime("%H:%M:%S")
        print(str(time) + ": Server is not connected")