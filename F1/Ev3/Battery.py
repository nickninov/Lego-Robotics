from ev3dev2.power import PowerSupply
from Actions import Actions
from threading import Thread
import time
from datetime import datetime

class Battery:

    def __init__(self, speed):
        self.minVoltage = PowerSupply().min_voltage
        self.maxVoltage = PowerSupply().max_voltage
        self.medVoltage = self.maxVoltage * 0.5
        self.exitVoltage = self.minVoltage + (self.minVoltage * 0.05)

        self.action = Actions(speed)

        # Get current time HH:MM:SS
        now = datetime.now()
        time = now.strftime("%H:%M:%S")

        print(str(time) + "\tExecuting Battery Thread\n")

        # Execute battery thread
        batteryThread = Thread(target=self.chargeStatus, args=())
        batteryThread.start()

    # Get current user's voltage
    def getCurrentVoltage(self):
        return PowerSupply().measured_voltage * 10

    # Check if Ev3 has to be charged
    def chargeStatus(self):
        while True:
            if self.getCurrentVoltage() <= self.exitVoltage:
                # Exit system
                self.action.exit()
            else:
                # Sleep for 1 min and 30 sec
                time.sleep(90)

    # Get the current percentage of the battery
    def getPercentage(self):
        percent = (self.getCurrentVoltage() / self.maxVoltage) * 100
        return str(round(percent))+"%"