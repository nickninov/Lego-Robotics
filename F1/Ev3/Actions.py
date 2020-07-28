from ev3dev2.motor import *
from datetime import datetime
import termios
import tty
import sys
import os

class Actions:
    def __init__(self, speed):
        self.leftMotor =  LargeMotor(OUTPUT_D)
        self.rightMotor = LargeMotor(OUTPUT_C)
        self.mediumMotor = MediumMotor(OUTPUT_A)
        self.speed = speed

    # Execute a terminal command as root user - requires command and password
    def terminalCommand(self, cmd):
        # For sudocommands without passwords - modified
        os.system("sudo "+cmd)

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

    # Stop Motors
    def stop(self):
        self.leftMotor.stop()
        self.rightMotor.stop()
        self.mediumMotor.stop()

    # Terminate program
    def exit(self):
        # Stop motors
        self.stop()

        # Get current time HH:MM:SS
        now = datetime.now()
        time = now.strftime("%H:%M:%S")

        print(str(time)+"\tTerminating program\n")
        self.terminalCommand("poweroff")
        # sys.exit(0)

    # Forward movement
    def forward(self):
        self.leftMotor.run_direct(duty_cycle_sp = -self.speed)
        self.rightMotor.run_direct(duty_cycle_sp = -self.speed)

    # Backward movement
    def backwards(self):
        self.leftMotor.run_direct(duty_cycle_sp = self.speed)
        self.rightMotor.run_direct(duty_cycle_sp = self.speed)

    # Turn left
    def left(self):
        self.mediumMotor.run_to_rel_pos(position_sp =  60, speed_sp = 300)
        self.mediumMotor.wait_while('running')
        self.mediumMotor.stop()

    # Turn right
    def right(self):
        self.mediumMotor.run_to_rel_pos(position_sp =  -60, speed_sp = 300)
        self.mediumMotor.wait_while('running')
        self.mediumMotor.stop()