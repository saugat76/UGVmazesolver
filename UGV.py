# From Ultrasonic Sensor we have  imported data type  List

import RPi.GPIO as gpio
import time
import PIN_Defination as PIN
from Ultrasonic_Sensor import readSensor


# import the check list from the processed image

def encoderCount(ENC_A_PIN, ENC_B_PIN):
    global count, count1, count2
    count1 = 0
    count2 = 0
    count = list
    gpioEn = gaugette.gpio.GPIO()
    encoder = gaugette.rotary_encoder.RotaryEncoder(gpioEn, ENC_A_PIN, ENC_B_PIN)
    while True:
        delta = encoder.get_delta()                                                 # returns 0,1,or -1
        if delta == 1:
            count += count1
        elif delta == -1:
            count -= count1
        else:
            pass
        return count


count1 = encoderCount(PIN.ENC_A1_PIN, PIN.ENC_B1_PIN)
count2 = encoderCount(PIN.ENC_A2_PIN, PIN.ENC_B2_PIN)


def init():
    gpio.setmode(gpio.BOARD)

    gpio.setup(PIN.MD_PIN_A, gpio.OUT)
    gpio.setup(PIN.MD_PIN_B, gpio.OUT)
    gpio.setup(PIN.MD_PIN_C, gpio.OUT)
    gpio.setup(PIN.MD_PIN_D, gpio.OUT)


def forward(tf):
    init()
    gpio.output(PIN.MD_PIN_A, False)
    gpio.output(PIN.MD_PIN_B, True)
    gpio.output(PIN.MD_PIN_C, True)
    gpio.output(PIN.MD_PIN_D, False)
    time.sleep(tf)

    gpio.cleanup()


def reverse(tf):
    init()
    gpio.output(PIN.MD_PIN_A, True)
    gpio.output(PIN.MD_PIN_B, False)
    gpio.output(PIN.MD_PIN_C, False)
    gpio.output(PIN.MD_PIN_D, True)
    time.sleep(tf)

    gpio.cleanup()


def turn_left(tf):
    init()
    gpio.output(PIN.MD_PIN_A, True)
    gpio.output(PIN.MD_PIN_B, True)
    gpio.output(PIN.MD_PIN_C, True)
    gpio.output(PIN.MD_PIN_D, False)
    time.sleep(tf)

    gpio.cleanup()


def turn_right(tf):
    init()
    gpio.output(PIN.MD_PIN_A, False)
    gpio.output(PIN.MD_PIN_B, True)
    gpio.output(PIN.MD_PIN_C, False)
    gpio.output(PIN.MD_PIN_D, False)
    time.sleep(tf)

    gpio.cleanup()


def pivot_left(tf):
    init()
    gpio.output(PIN.MD_PIN_A, True)
    gpio.output(PIN.MD_PIN_B, False)
    gpio.output(PIN.MD_PIN_C, True)
    gpio.output(PIN.MD_PIN_D, False)
    time.sleep(tf)

    gpio.cleanup()


def pivot_right(tf):
    init()
    gpio.output(PIN.MD_PIN_A, False)
    gpio.output(PIN.MD_PIN_B, True)
    gpio.output(PIN.MD_PIN_C, False)
    gpio.output(PIN.MD_PIN_D, True)
    time.sleep(tf)

    gpio.cleanup()


def decisionCheck():
    if left_distance < PIN.DIST_LIMIT and right_distance < PIN.DIST_LIMIT and front_distance < PIN.DIST_LIMIT:
        decision = False
        print("Dead End Reached")
    elif front_distance < PIN.DIST_LIMIT and (right_distance < PIN.DIST_LIMIT or left_distance < PIN.DIST_LIMIT):
        decision = True
    elif right_distance < PIN.DIST_LIMIT and left_distance < PIN.DIST_LIMIT:
        decision = False
    elif left_distance >= PIN.DIST_LIMIT and right_distance >= PIN.DIST_LIMIT and front_distance >= PIN.DIST_LIMIT:
        decision = False
        print("UGV is in Start or Finish")
    else:
        decision = True

    return decision


count = 0
while True:
    tf = 0.01
    currentDistance = readSensor()
    front_distance = currentDistance[0]
    right_distance = currentDistance[1]
    left_distance = currentDistance[2]
    decisionValue = decisionCheck()
    if decisionValue:
        if checkSet[count] == 0:
            pivot_left(tf)
        # elif checkSet[count] == 1:
        #    forward(tf)
        elif checkSet[count] == 1:
            pivot_right(tf)
        count = count + 1
    else:
        forward(tf)
