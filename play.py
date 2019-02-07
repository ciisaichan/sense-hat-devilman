#!/usr/bin/python
import os
import time
from sense_hat import SenseHat

sense = SenseHat()
sense.clear()

def play_frame():
    fDir = './frame/'
    var = sum([len(x) for _, _, x in os.walk(os.path.dirname(fDir))])
    x = 0
    while x < var:
        sense.load_image(fDir + str('%05d' % x) + '.jpg')
        time.sleep(0.036)
        x = x + 1
    sense.clear()

print('Press down the joystick to start.')
while True:
    for event in sense.stick.get_events():
        if event.direction == 'middle':
            print('playing...')
            play_frame()
            print('end.')
            exit()
