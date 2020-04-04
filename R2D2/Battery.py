from ev3dev2.power import PowerSupply
from ev3dev2.motor import *
from threading import Thread
import os
import time

class Battery:

    def __init__(self):
        self.minVoltage = PowerSupply().min_voltage
        self.maxVoltage = PowerSupply().max_voltage
        self.medVoltage = self.maxVoltage * 0.5
        self.exitVoltage = self.minVoltage + (self.minVoltage * 0.05)

        self.leftMotor =  LargeMotor(OUTPUT_A)
        self.rightMotor = LargeMotor(OUTPUT_D)
        self.mediumMotor = MediumMotor(OUTPUT_C)

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
                self.mediumMotor.stop()
                self.leftMotor.stop()
                self.rightMotor.stop()
                os._exit(0)
            else:
                # Sleep for 1 min and 30 sec
                time.sleep(90)