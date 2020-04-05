from ev3dev2.sensor.lego import TouchSensor
from threading import Thread
from Movement import Movement
import os

class Button:

    def __init__(self):
        self.button = TouchSensor()

        self.move = Movement()

        print("Starting button thread")

        # Execute button thread
        buttonThread = Thread(target=self.isPressed, args=())
        buttonThread.start()

    # Check if Ev3 button was pressed and program has to terminate
    def isPressed (self):
        while True:
            if self.button.is_pressed == True:
                self.move.exit()