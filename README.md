# LittleYellowRobot
Setup guide and code for the little yellow robot retro-fit

## LIRC
First, you will need an IR receiver (I have used a TSOP38238, from eBay) and get that setup on your Raspberry Pi. Both [this guide](https://www.hackster.io/duculete/ir-remote-with-raspberry-pi-d5cf5f) and [this one]() walk you through everything you need (and probably more) for all of that, but in short
- `sudo apt-get install lirc`
- Edit `/etc/modules` (only using the `gpio_in_pin` argument, as we aren't transmitting)
- Edit `/etc/lirc/hardware.conf`

## Python
This repository assumes specific pins are in use for the code. If you are using different components, these may have to change:
- for the motor board, the [Pololu DRV8835](https://www.pololu.com/product/2753), the BCM pins used are 5, 6, 12 and 13;
- the eyes of the robot are wired onto BCM 21 and the ground pin 40 next to it;
- the IR receiver is wired onto 5v pin 2, ground on pin 6 and BCM pin 17

## In use
When the robot it switched on, it should pulse its eyes when ready to receive commands.
On the PS2 remote, numbers 1-0 change the power being sent to the motors (1 is 10%, 9 is 90%). Steering is done with the direction keys and it is programmed to power off when you press `STOP` on the remote. 
