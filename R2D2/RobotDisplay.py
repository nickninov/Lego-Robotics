import os
import ev3dev2.fonts as fonts
from time import sleep
from ev3dev2.display import *
from PIL import Image, ImageDraw, ImageFont

class RobotDisplay:

    def __init__(self, password):
        self.password = password

        # Ev3 display
        self.screen = Display()

        # Load font - put your own path to font location
        self.font = ImageFont.truetype('/home/robot/myproject/Fonts/Verdana.ttf', 100)

    # Execute a terminal command as root user - requires command and password
    def terminalCommand(self, cmd):
        # For sudo commands with password
        # os.popen("echo %s | sudo -S %s" % (self.password, cmd)).read()

        # For sudocommands without passwords - modified
        os.system("sudo "+cmd)

    # Start screen
    def startScreen(self):
        self.terminalCommand("chvt 6")
        self.drawText("")

    # Stop brickman
    def exit(self):
        self.terminalCommand("poweroff")

    # Draw text on screen
    def drawText(self, str):
        self.screen.clear()
        if len(str) == 2:
            self.screen.draw.text((25, 0), str, font = self.font)
            self.screen.update()
        elif len(str) == 1:
            self.screen.draw.text((60, 0), str, font=self.font)
            self.screen.update()
        else:
            self.screen.draw.text((0, 0), str, font=self.font)
            self.screen.update()
