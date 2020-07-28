from ev3dev2.sensor.lego import TouchSensor
from threading import Thread
from Actions import Actions
from datetime import datetime

class Button:

    def __init__(self, speed):
        self.button = TouchSensor()
        self.action = Actions(speed)

        # Get current time HH:MM:SS
        now = datetime.now()
        time = now.strftime("%H:%M:%S")

        print(str(time) + "\tExecuting Touch Sensor Thread\n")

        # Execute button thread
        buttonThread = Thread(target=self.isPressed, args=())
        buttonThread.start()

    # Check if Ev3 button was pressed and program has to terminate
    def isPressed (self):
        while True:
            if self.button.is_pressed == True:
                # Exit system
                self.action.exit()