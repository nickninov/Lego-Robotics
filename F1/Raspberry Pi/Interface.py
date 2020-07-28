from tkinter import *
from datetime import datetime
from PIL import Image, ImageTk
import tkinter as tki
import threading
import imutils
import cv2
import os
import requests

class Interface:
    # Require instance of VideoStream and the path to where to store the snapshot
    def __init__(self, vs, outputPath):
        # IP address of Ev3
        self.ev3IP = 'http://192.168.1.10:5000'

        self.vs = vs
        self.outputPath = outputPath

        # Read frame
        self.frame = None

        # Control video loop
        self.thread = None
        self.stopEvent = None
        self.panel = None

        # Button icons subsample size
        self.subsample = 11

        # Create window
        self.window = Tk()

        # Set key binds
        # Q - exit program
        self.window.bind('q', self.exitProgram)

        # E - take a snapshot
        self.window.bind('e', self.snapshot)

        # W - move formula forward
        self.window.bind('w', self.forward)

        # S - move formula backwards
        self.window.bind('s', self.backwards)

        # D - turn front wheels right
        self.window.bind('d', self.turnRight)

        # A - turn front wheels right
        self.window.bind('a', self.turnLeft)

        # <Space> - stop F1 engines
        self.window.bind('<space>', self.stop)

        # Set window's title
        self.window.title("Ev3 Formula 1")

        # Disable window resizing
        self.window.resizable(width=False, height=False)

        self.batteryLabel = Label(self.window,text="")
        self.batteryLabel.config(font=("Courier", 33))
        self.batteryLabel.pack(side=BOTTOM, anchor='center', pady=30)

        # Frame for camera input and output console
        self.camFrame = Frame(self.window)
        self.camFrame.pack()

        # Start video thread
        self.stopEvent = threading.Event()
        self.thread = threading.Thread(target=self.videoLoop, args=())
        self.thread.start()

        # Scrollbar for the list
        self.scroll = Scrollbar(self.camFrame, orient=VERTICAL)

        # A list box that will show the actions the user has done
        self.history = Listbox(self.camFrame, width=35, yscrollcommand=self.scroll.set)

        # Configure scrollbar
        self.scroll.config(command=self.history.yview)
        self.scroll.pack(side=RIGHT, fill='y')
        self.history.pack(side=RIGHT, fill='y')

        # Frame for buttons
        self.btnFrame = Frame(self.window)
        self.btnFrame.pack(side=BOTTOM, fill='x')

        # Frame for arrows
        self.arrowFrame = Frame(self.btnFrame)
        self.arrowFrame.pack(anchor='center')

        # Up Button
        self.upPhoto = PhotoImage(file=r"img/up.png")
        self.upImg = self.upPhoto.subsample(self.subsample, self.subsample)
        self.upBtn = Button(self.arrowFrame, image=self.upImg, command = self.forward)
        self.upBtn.grid(row=0, column=1)

        # Left Button
        self.leftPhoto = PhotoImage(file=r"img/left.png")
        self.leftImg = self.leftPhoto.subsample(self.subsample, self.subsample)
        self.leftBtn = Button(self.arrowFrame, image=self.leftImg, command = self.turnLeft)
        self.leftBtn.grid(row=1, column=0)

        # Down Button
        self.dowmPhoto = PhotoImage(file=r"img/down.png")
        self.downImg = self.dowmPhoto.subsample(self.subsample, self.subsample)
        self.downBtn = Button(self.arrowFrame, image=self.downImg, command = self.backwards)
        self.downBtn.grid(row=1, column=1)

        # Right Button
        self.rightPhoto = PhotoImage(file=r"img/right.png")
        self.rightImg = self.rightPhoto.subsample(self.subsample, self.subsample)
        self.rightBtn = Button(self.arrowFrame, image=self.rightImg, command = self.turnRight)
        self.rightBtn.grid(row=1, column=2)

        # Record frame
        self.snapshotFrame = LabelFrame(self.arrowFrame, text="Snapshot")
        self.snapshotFrame.grid(row=2, column=2)

        # Record button
        self.snapshotPhoto = PhotoImage(file=r"img/record.png")
        self.snapshotImg = self.snapshotPhoto.subsample(self.subsample, self.subsample)
        self.snapshotBtn = Button(self.snapshotFrame, image=self.snapshotImg, command = self.snapshot)
        self.snapshotBtn.pack()

        # Exit frame
        self.exitFrame = LabelFrame(self.arrowFrame, text="Exit")
        self.exitFrame.grid(row=2, column=0)

        # Exit button
        self.exitPhoto = PhotoImage(file=r"img/exit.png")
        self.exitImg = self.exitPhoto.subsample(self.subsample, self.subsample)
        self.exitBtn = Button(self.exitFrame, image=self.exitImg, command = self.exitProgram)
        self.exitBtn.pack()

        # Stop frame
        self.stopFrame = LabelFrame(self.arrowFrame, text="Stop")
        self.stopFrame.grid(row=2,column=1)

        # Stop button
        self.stopPhoto = PhotoImage(file=r"img/stop.png")
        self.stopImg = self.stopPhoto.subsample(self.subsample, self.subsample)
        self.stopBtn = Button(self.stopFrame, image=self.stopImg, command = self.stop)
        self.stopBtn.pack()

        # Run window
        self.window.mainloop()

    # Display video output
    def videoLoop(self):
        try:
            # Loop frames until stopped
            while not self.stopEvent.is_set():
                # Take a frame from the video stream and resize
                self.frame = self.vs.read()
                self.frame = imutils.resize(self.frame, width=800)

                # Convert image to PIL and ImageTk
                image = cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB)
                image = Image.fromarray(image)
                image = ImageTk.PhotoImage(image)

                # Check if panel needs to be initialized
                if self.panel is None:
                    self.panel = tki.Label(self.camFrame, image=image)
                    self.panel.image = image
                    self.panel.pack(padx=10, pady=10)

                # Update panel
                else:
                    self.panel.configure(image=image)
                    self.panel.image = image

        except RuntimeError:
            str = self.getTime() + "\t\tRuntimeError"
            self.history.insert(END, str)
            self.history.insert(END, "")

    # Take a snapshot of the current frame
    def takeSnapshot(self):
        # Output path is the current timestamp
        ts = datetime.now()
        filename = "{}.jpg".format(ts.strftime("%Y-%m-%d_%H-%M-%S"))
        p = os.path.sep.join((self.outputPath, filename))

        # Save file
        cv2.imwrite(p, self.frame.copy())
        str = self.getTime() + "\t\t"+filename
        self.history.insert(END, str)

    # Get current time HH:MM:SS
    def getTime(self):
        now = datetime.now()
        time = now.strftime("%H:%M:%S")
        return str(time)

    # Exit program
    def exitProgram(self, event = None):
        # Stop video output
        self.stopEvent.set()
        self.vs.stop()

        # Terminate battery thread
        self.isActive = False

        # Shut down Ev3
        url = self.ev3IP + "/GET/Ev3/F1/movement/exit"
        self.apiFetch(url)

    # Take a picture
    def snapshot(self, event = None):
        # Take a snapshot and save it
        self.takeSnapshot()

        str = self.getTime() + "\t\tPicture taken"
        self.history.insert(END, str)
        self.history.insert(END, "")

    # Move Formula forward
    def forward(self, event = None):
        # API url
        url = self.ev3IP + "/GET/Ev3/F1/movement/forward"

        # API GET thread
        t = threading.Thread(target=self.apiFetch, args=(url,))
        t.start()

    # Move Formula backwards
    def backwards(self, event = None):
        # API url
        url = self.ev3IP + "/GET/Ev3/F1/movement/backward"

        # API GET thread
        t = threading.Thread(target=self.apiFetch, args=(url, ))
        t.start()

    # Turn front wheels left
    def turnLeft(self, event = None):
        # API url
        url = self.ev3IP + "/GET/Ev3/F1/movement/left"

        # API GET thread
        t = threading.Thread(target=self.apiFetch, args=(url, ))
        t.start()

    # Turn front wheels right
    def turnRight(self, event = None):
        # API url
        url = self.ev3IP + "/GET/Ev3/F1/movement/right"

        # API GET thread
        t = threading.Thread(target=self.apiFetch, args=(url,))
        t.start()

    # Stop engines
    def stop(self, event = None):
        # API url
        url = self.ev3IP + "/GET/Ev3/F1/movement/stop"

        # API GET thread
        t = threading.Thread(target=self.apiFetch, args=(url,))
        t.start()

    # API GET request
    def apiFetch(self, url):
        # GET request to EV3
        data = requests.get(url).json()

        # Check if fetch was successful
        if data['status'] == 200:
            self.batteryLabel["text"] = data['percent']
            str = data['time'] + "\t\tMovement\t\t" + data['direction']
            self.history.insert(END, str)
            self.history.insert(END, "")