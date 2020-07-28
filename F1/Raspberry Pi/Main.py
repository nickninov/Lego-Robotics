from Interface import Interface
from imutils.video import VideoStream
import argparse
import time

# python Main.py - -output output
if __name__ == "__main__":
    # Construct the argument parse and parse the arguments
    ap = argparse.ArgumentParser()
    ap.add_argument("-o", "--output", required=True, help="path to output directory to store snapshots")
    ap.add_argument("-p", "--picamera", type=int, default=-1, help="whether or not the Raspberry Pi camera should be used")
    args = vars(ap.parse_args())

    # Initialize the video stream and launch the camera
    print("Launching camera")
    vs = VideoStream(usePiCamera=args["picamera"] > 0).start()
    time.sleep(2.0)

    # Launch GUI
    window = Interface(vs, "/home/pi/Desktop/Ev3/F1/snapshots/")