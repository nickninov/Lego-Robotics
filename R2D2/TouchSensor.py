from ev3dev2.sensor.lego import TouchSensor
from threading import Thread
from Actions import Actions
import os

class Button:

    def __init__(self, client, display):
        self.button = TouchSensor()

        self.action = Actions()

        self.client = client
        self.display = display

        print("Starting button thread")

        # Execute button thread
        buttonThread = Thread(target=self.isPressed, args=())
        buttonThread.start()

    # Check if Ev3 button was pressed and program has to terminate
    def isPressed (self):
        while True:
            if self.button.is_pressed == True:
                # Exit system
                self.action.exit(self.client, self.display)