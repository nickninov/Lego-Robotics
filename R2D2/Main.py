from Battery import Battery
from TouchSensor import Button
from Movement import Movement
from ev3dev2.sound import Sound
from threading import Thread

if __name__ == '__main__':

    # Declaring variables
    battery = Battery() # Starting battery thread
    button = Button() # Starting button thread
    sound = Sound()
    move = Movement()

    def readySound():
        sound.play_file("Sounds/1.wav", 100, Sound.PLAY_WAIT_FOR_COMPLETE)

    readyThread = Thread(target=readySound, args=())
    readyThread.start()

    print("Start main thread\n")

    while True:

        move.movement()