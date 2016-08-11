#!/usr/bin/python2
import lirc
from gpiozero import Robot

motor = False
sockid = lirc.init("robot", "lirc/robot-lircrc", blocking=False)

# Using the lircd interface...
while True:
    codeIR = lirc.nextcode()
    if codeIR:
        print("Received (", len(codeIR), "):", codeIR[0])
        motor = True
    elif motor == True:
        print("Stop motor")
        motor = False
