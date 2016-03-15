#!/usr/bin/python3
from gpiozero import Robot
from evdev import InputDevice, list_devices, ecodes

# Set up the GPIOZero robot instance
robot = Robot(left=(6,19), right=(17,22))
remote_actions = {
    ecodes.KEY_UP : robot.forward,
    ecodes.KEY_DOWN : robot.backward,
    ecodes.KEY_LEFT : robot.left,
    ecodes.KEY_RIGHT : robot.right
}

# Process the (lirc-spawned) events
device = InputDevice("/dev/input/event0")
for event in device.read_loop():
    if event.type == ecodes.EV_KEY:
        if event.value == 1: # key down
            remote_actions[event.code]()
        elif event.value == 0: # key up
            robot.stop()
