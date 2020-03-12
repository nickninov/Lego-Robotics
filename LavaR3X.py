import ev3dev2 as ev3
from ev3dev2.sound import *
from ev3dev2.motor import *
from ev3dev2.led import *
from time import sleep
from threading import Thread
import random

print("Start")

leftMotor =  LargeMotor(OUTPUT_D) # Left Motor
rightMotor = LargeMotor(OUTPUT_B) # Right Motor
mediumMotor = MediumMotor(OUTPUT_A) # Head Motor

# Play song
def playSong(name):
    sound = Sound();  # For music
    print("Playing " + name)
    # Reduce Sample Rate - 8kHz
    # Reduce bits per sample
    sound.play(name);


# Moves forward for the given degrees and given speed
def walkForward(degrees, speed):
    leftMotor.run_to_rel_pos(position_sp=degrees, speed_sp=speed)
    rightMotor.run_to_rel_pos(position_sp=degrees, speed_sp=speed)
    rightMotor.wait_while('running')
    leftMotor.wait_while('running')

# Moves backwards for the given degrees and given speed
def walkBackwards(degrees, speed):
    leftMotor.run_to_rel_pos(position_sp=-degrees, speed_sp=speed)
    rightMotor.run_to_rel_pos(position_sp=-degrees, speed_sp=speed)
    rightMotor.wait_while('running')
    leftMotor.wait_while('running')

# Turn left
def turnLeft(degrees, speed):
    rightMotor.run_to_rel_pos(position_sp=-degrees, speed_sp=speed)
    rightMotor.wait_while('running')

# Turn right
def turnRight(degrees, speed):
    leftMotor.run_to_rel_pos(position_sp=-degrees, speed_sp=speed)
    leftMotor.wait_while('running')

# Turn head left
def turnUpperbodyLeft(degrees, speed):
    mediumMotor.run_to_rel_pos(position_sp=degrees, speed_sp=speed)
    mediumMotor.wait_while('running')

# Turn head right
def turnUpperbodyRight(degrees, speed):
    mediumMotor.run_to_rel_pos(position_sp= -degrees, speed_sp=speed)
    mediumMotor.wait_while('running')

# Returns a random color
def getRandomColor():
    randomColor = random.randint(0, 5)
    # Get a random color
    if randomColor == 0:
        return 'RED'

    elif randomColor == 1:
        return 'GREEN'

    elif randomColor == 2:
        return'YELLOW'

    elif randomColor == 3:
        return 'ORANGE'

    elif randomColor == 4:
        return 'AMBER'

    elif randomColor == 5:
        return 'BLACK'

# Returna random LED
def getRandomLed():
    randomLed = random.randint(0, 1)
    # Get a random LED
    if randomLed == 0:
        return 'LEFT'
    else:
        return 'RIGHT'


# Change light color
def ledShow(seconds):
    leds = Leds()  # For led colors
    for second in range(seconds):

        color = getRandomColor()

        # Set LEDS
        leds.set_color('LEFT', color);
        leds.set_color('RIGHT', color);
        sleep(1)
        leds.all_off()

# A function that makes the robot dance
def dance(times):
    for i in range(times):
        walkForward(360, 200)
        walkBackwards(360, 200)

def bodyMovement(times):

    # Turn head from straight to left
    turnUpperbodyLeft(200, 300)

    # Start movement right to left
    for i in range(times - 1):
        turnUpperbodyRight(400, 300)
        turnUpperbodyLeft(400, 300)


# Execute dance thread
print("Executing Thread 1")
t1 = Thread(target = dance, args = (8,))
t1.start()
print("Thread 1 has started - Dancing")

# Execute LED show thread
print("Executing Thread 2")
t2 = Thread(target = ledShow, args = (30,))
t2.start()
print("Thread 2 has started - LEDs")

# Execute the upper body movement thread
print("Executing Thread 3")
t3 = Thread(target=bodyMovement, args=(13,))
t3.start()
print("Thread 3 has started - Upper body movement")

# Play song
playSong('skrillex.wav')