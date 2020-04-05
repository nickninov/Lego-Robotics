from ev3dev2.power import PowerSupply
from ev3dev2.motor import *
from Movement import Movement
from threading import Thread
import os
import time

class Battery:

    def __init__(self):
        self.minVoltage = PowerSupply().min_voltage
        self.maxVoltage = PowerSupply().max_voltage
        self.medVoltage = self.maxVoltage * 0.5
        self.exitVoltage = self.minVoltage + (self.minVoltage * 0.05)

        self.move = Movement()

        print("Starting battery thread")

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
                self.move.exit()
            else:
                # Sleep for 1 min and 30 sec
                time.sleep(90)