# Python Robotics

## Launch Ev3
Terminal command:<br>`ssh robot@ev3dev.local`
<br><br>Password:<br>`maker`
### Run sudo commands without asking Ev3 for a password
1) When you SSH in to the Ev3 type <br>`sudo visudo`
2) In the bottom of the file - below **#includedir /etc/sudoers.d**, add <br>`username ALL=(ALL) NOPASSWD: ALL`<br>To check what is your robot's username type <br>`whoami`
3) Exit and save the file

# R2-D2
This project allows the user to control R2-D2 through the keyboard and ask it what the weather is. <br>
* Key **0** - Stops the motors
* Key **Q** - Stops the server and shuts down Ev3
* Key **E** - Tells the weather
* Key **W** - Goes forward
* Key **S** - Goes backward
* Key **A** - Turns left and goes forward
* Key **D** - Turns right and goes forward
* **R2-D2 TouchSensor** - Stops the server and shuts down Ev3

**How to launch:**
 1) Launch Server.py <br> `python3 Server.py` <br>
 2) Launch Main.py <br> `python3 Main.py`


# F1
This project allows the user to remotely control the Lego F1 from a Raspberry Pi from a GUI and take pictures with the Raspberry Pi camera. <br>

* Key **Q** - Exit program
* Key **E** - Snapshot
* Key **W** - Go forward
* Key **S** - Go backwards
* Key **A** - Turn left
* Key **D** - Turn right
* Key **Space** - Stop motors

**How to launch:**
1) Launch Ev3 <br> `python3 Main.py`

2) Launch Raspberry Pi
* `LD_PRELOAD=/usr/lib/arm-linux-gnueabihf/libatomic.so.1 python3`
* import os <br>
* os.system('python3 Main.py --output output')
