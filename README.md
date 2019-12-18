# PiNoiseBox

This project is a simple sound box using arcade buttons and the GPIO pins on a Raspberry Pi. 

Requirements
-Raspberry Pi
-Python3
-Arcade buttons or momentary switches
-Breadboard and jumper wires

To auto launch the python script at startup, I simply added this line to the /etc/profile file:
'sudo python3 /gpio-soundboard/soundfx/soundfx.py'

The python script uses a button module to interface with the GPIO pins and map them to sound files.