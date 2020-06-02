# Python Robotics

## Launch Ev3
Terminal command:<br>`ssh robot@ev3dev.local`
<br><br>Password:<br>`maker`
### Run sudo commands without asking Ev3 for a password
1) When you SSH in to the Ev3 type <br>`sudo visudo`
2) In the bottom of the file - below **#includedir /etc/sudoers.d**, add <br>`username ALL=(ALL) NOPASSWD: ALL`<br>To check what is your robot's username write <br>`whoami`
3) Exit and save the file

### R2-D2
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
