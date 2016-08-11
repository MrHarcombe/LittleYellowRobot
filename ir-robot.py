#!/usr/bin/python2
from gpiozero import PWMLED, PhaseEnableRobot
from evdev import InputDevice, list_devices, ecodes
import sys
import os

# Set up the GPIOZero robot instance
robot = PhaseEnableRobot()

robot_movement = {
    ecodes.KEY_UP : robot.forward,
    ecodes.KEY_DOWN : robot.backward,
    ecodes.KEY_LEFT : robot.left,
    ecodes.KEY_RIGHT : robot.right,
}

robot_power = (
    ecodes.KEY_1,
    ecodes.KEY_2,
    ecodes.KEY_3,
    ecodes.KEY_4,
    ecodes.KEY_5,
    ecodes.KEY_6,
    ecodes.KEY_7,
    ecodes.KEY_8,
    ecodes.KEY_9,
    ecodes.KEY_0,
)

evdev_device = 0
try:
    evdev_device = int(sys.argv[1])
except IndexError:
    pass
except ValueError:
    pass


print("Almost there, pulse the eyes to let the user know")
eyes = PWMLED(21)
eyes.blink(0.5, 0.25, 0.25, 0.25, 3, False)
eyes.on()

print("Initialised, now handling events")
try:
    # Only run the motors at 50% initially
    power = 0.5
 
    # Process the (lirc-spawned) events
    device = InputDevice("/dev/input/event" + str(evdev_device))
    for event in device.read_loop():
        if event.type == ecodes.EV_KEY:
            if event.value == 1: # key down
                if event.code in robot_movement:
                    robot_movement[event.code](power)
                elif event.code in robot_power:
                    power = (event.code - 1) / 10
                elif event.code == ecodes.KEY_ENTER:
                    robot.stop()
                elif event.code == ecodes.KEY_STOP:
                    print("Powering off...")
                    os.execl("poweroff")
            elif event.value == 2: # key held
                if event.code in robot_movement:
                    robot_movement[event.code](power)
            elif event.value == 0: # key up
                if event.code in robot_movement:
                    robot.stop()

except KeyboardInterrupt:
    print("heerio")
