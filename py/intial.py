#!/usr/bin/env python

# Copyright (c) 2019, NVIDIA CORPORATION. All rights reserved.
# Permission is hereby granted, free of charge, to any person obtaining a
# copy of this software and associated documentation files (the "Software"),
# to deal in the Software without restriction, including without limitation
# the rights to use, copy, modify, merge, publish, distribute, sublicense,
# and/or sell copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.  IN NO EVENT SHALL
# THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
# DEALINGS IN THE SOFTWARE.

import RPi.GPIO as GPIO
import time


# Pin Definitions
output_pin1 = 12  #ALRAM  BCM pin 18, BOARD pin 12
output_pin2 = 16  #LED

def main():
    # Pin Setup:
    GPIO.setmode(GPIO.BOARD)  # BCM pin-numbering scheme from Raspberry Pi
    # set pin as an output pin with optional initial state of HIGH
    GPIO.setup(output_pin1, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(output_pin2, GPIO.OUT, initial=GPIO.LOW)

    print("Starting demo now! Press CTRL+C to exit")
    flag1 = GPIO.LOW
    flag2 = GPIO.LOW
    delay = 0
    try:
        while True:
            
            time.sleep(0.5)
            if (delay == 0):
                if (flag1 == GPIO.LOW):
                    flag1 = GPIO.HIGH
                else:
                    flag1 = GPIO.LOW
                GPIO.output(output_pin1, flag1)

            if (flag2 == GPIO.LOW):
                flag2 = GPIO.HIGH
            else:
                flag2 = GPIO.LOW
            GPIO.output(output_pin2, flag2)
            delay += 1
            if delay == 2:delay = 0
    finally:
        GPIO.cleanup()

if __name__ == '__main__':
    main()
