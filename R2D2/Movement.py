from ev3dev2.motor import *
import termios
import tty
import os
import sys
from datetime import datetime

class Movement:
    def __init__(self):
        self.leftMotor =  LargeMotor(OUTPUT_A)
        self.rightMotor = LargeMotor(OUTPUT_D)
        self.mediumMotor = MediumMotor(OUTPUT_C)


    # Gets the current pressed key
    def getch(self):
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

        return ch

    # Move Character
    def movement(self):
        # Get user's input
        k = self.getch()

        # Get current time HH:MM:SS
        now = datetime.now()
        time = now.strftime("%H:%M:%S")

        # Exit
        if k == 'q':
            self.mediumMotor.stop()
            self.leftMotor.stop()
            self.rightMotor.stop()
            print(str(time)+": Exit program")
            os._exit(0)

        # Go forward
        if k == 'w':
            self.leftMotor.run_direct(duty_cycle_sp = -50)
            self.rightMotor.run_direct(duty_cycle_sp = -50)
            print(str(time) + ": Go forward")
        # Go backwards
        elif k == 's':
            self.leftMotor.run_direct(duty_cycle_sp = 50)
            self.rightMotor.run_direct(duty_cycle_sp = 50)
            print(str(time) + ": Go backwards")
        # Go left
        elif k == 'a':
            self.leftMotor.run_to_rel_pos(position_sp=-320, speed_sp=400)
            self.rightMotor.run_to_rel_pos(position_sp=320, speed_sp=400)
            print(str(time) + ": Turn left")
        # Go right
        elif k == 'd':
            self.leftMotor.run_to_rel_pos(position_sp=320, speed_sp=400)
            self.rightMotor.run_to_rel_pos(position_sp=-320, speed_sp=400)
            print(str(time) + ": Turn right")