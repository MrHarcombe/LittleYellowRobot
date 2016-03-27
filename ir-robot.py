#!/usr/bin/python3
from gpiozero import PololuRobot
from evdev import InputDevice, list_devices, ecodes
import sys

# Set up the GPIOZero robot instance
robot = PololuRobot(left=(12,5), right=(13,6))

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
if (len(sys.argv) > 0):
  if sys.argv[0].is_digit():
    evdev_device = int(sys.argv[0])

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
                    # print("Moving at power:", power)
                    robot_movement[event.code](power)
                elif event.code in robot_power:
                    # print("Setting power to:", event.code - 1)
                    power = (event.code - 1) / 10
                elif event.code == ecodes.KEY_ENTER:
                    # print("Stopping due to Enter key pressed")
                    robot.stop()
            elif event.value == 2: # key held
                # print("Held, continuing at power:", power)
                if event.code in robot_movement:
                    robot_movement[event.code](power)
            elif event.value == 0: # key up
                if event.code in robot_movement:
                    # print("Stopping due to movement key released")
                    robot.stop()

except KeyboardInterrupt:
    print("heerio")
