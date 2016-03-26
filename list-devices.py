#!/usr/bin/python3
from evdev import InputDevice, list_devices, ecodes, categorize

devices = [InputDevice(fn) for fn in list_devices()]
for device in devices:
    print(device.fn, device.name, device.phys)
