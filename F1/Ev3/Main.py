from flask import Flask, jsonify
from datetime import datetime
from Actions import Actions
from TouchSensor import Button
from Battery import Battery

# Initialize movement speed
speed = 100

# Start Touch Sensor thread
button = Button(speed)

# Start Battery thread
battery = Battery(speed)

# Declare movement
actions = Actions(speed)

# Get current time HH:MM:SS
now = datetime.now()
time = str(now.strftime("%H:%M:%S"))

print(time + "\tLaunching program\n")

app = Flask (__name__)

# Move vehicle in the given direction
@app.route('/GET/Ev3/F1/movement/<action>', methods = ['GET'])
def movement(action):

    # Get current time HH:MM:SS
    now = datetime.now()
    time = str(now.strftime("%H:%M:%S"))

    # Check if current action is valid
    if action == "forward" or action == "backward" or action == "left" or action == "right" or action == "stop" or action == "exit":

        # Check if Ev3 should go forward
        if action == "forward":
            # Move forward
            actions.forward()

            return jsonify({
                'status': 200,
                'direction': 'Forward',
                'time': time,
                'percent': battery.getPercentage()
            })

        # Check if Ev3 should go backwards
        elif action == "backward":
            # Move backwards
            actions.backwards()

            return jsonify({
                'status': 200,
                'direction': 'Backwards',
                'time': time,
                'percent': battery.getPercentage()
            })

        # Check if Ev3 should turn left
        elif action == "left":
            # Turn left
            actions.left()

            return jsonify({
                'status': 200,
                'direction': 'Left',
                'time': time,
                'percent': battery.getPercentage()
            })

        # Check if Ev3 should turn right
        elif action == "right":
            # Turn right
            actions.right()

            return jsonify({
                'status': 200,
                'direction': 'Right',
                'time': time,
                'percent': battery.getPercentage()
            })

        # Check if Ev3 should stop englines
        elif action == "stop":
            # Stop engines
            actions.stop()

            return jsonify({
                'status': 200,
                'direction': 'Stop engines',
                'time': time,
                'percent': battery.getPercentage()
            })

        # Check if Ev3 should shut down
        elif action == "exit":
            # Shut down Ev3
            actions.exit()
            return jsonify({
                'status': 200,
                'direction': 'Shut down Ev3',
                'time': time,
                'percent': battery.getPercentage(),
            })
    else:
        return jsonify({
            'status': 404,
            'direction': 'N/A',
            'time': time,
            'percent': battery.getPercentage(),
        })

app.run(debug=True, host='0.0.0.0')