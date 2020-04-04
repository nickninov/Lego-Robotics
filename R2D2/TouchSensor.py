from ev3dev2.sensor.lego import TouchSensor
from ev3dev2.motor import *
from threading import Thread
import os

class Button:

    def __init__(self):
        self.button = TouchSensor()

        self.leftMotor =  LargeMotor(OUTPUT_A)
        self.rightMotor = LargeMotor(OUTPUT_D)
        self.mediumMotor = MediumMotor(OUTPUT_C)

        print("Starting button thread")

        # Execute button thread
        buttonThread = Thread(target=self.isPressed, args=())
        buttonThread.start()

    # Check if Ev3 button was pressed and program has to terminate
    def isPressed (self):
        while True:
            if self.button.is_pressed == True:
                self.mediumMotor.stop()
                self.leftMotor.stop()
                self.rightMotor.stop()
                os._exit(0)