from Battery import Battery
from TouchSensor import Button
from Movement import Movement
from ev3dev2.sound import Sound


if __name__ == '__main__':

    # Declaring variables
    battery = Battery() # Starting battery thread
    button = Button() # Starting button thread
    sound = Sound()
    move = Movement()
    print("Start main thread\n")

    while True:

        move.movement()
        # sound.play_file("Sounds/1.wav", 100, Sound.PLAY_WAIT_FOR_COMPLETE)
        # sound.play_file("Sounds/2.wav", 100, Sound.PLAY_WAIT_FOR_COMPLETE)
        # sound.play_file("Sounds/3.wav", 100, Sound.PLAY_WAIT_FOR_COMPLETE)
        # sound.play_file("Sounds/4.wav", 100, Sound.PLAY_WAIT_FOR_COMPLETE)

    print("Exit program")

