import RPi.GPIO as gpio
import time
import PIN_Defination as PIN


def readSensor():
    gpio.setmode(gpio.BOARD)

    # Sensor PIN Mode Defination
    gpio.setup(PIN.US_SENSOR_FRONT_TRIG, gpio.OUT)
    gpio.setup(PIN.US_SENSOR_FRONT_ECHO, gpio.IN)

    gpio.setup(PIN.US_SENSOR_RIGHT_TRIG, gpio.OUT)
    gpio.setup(PIN.US_SENSOR_RIGHT_ECHO, gpio.IN)

    gpio.setup(PIN.US_SENSOR_LEFT_TRIG, gpio.OUT)
    gpio.setup(PIN.US_SENSOR_LEFT_ECHO, gpio.IN)

    gpio.output(PIN.US_SENSOR_FRONT_TRIG, False)
    gpio.output(PIN.US_SENSOR_LEFT_TRIG, False)
    gpio.output(PIN.US_SENSOR_RIGHT_TRIG, False)

    def measure(echoPIN):
        while gpio.input(echoPIN) == 0:
            no_signal = time.time()

        while gpio.input(echoPIN) == 1:
            signal = time.time()

        time_measured = signal - no_signal
        distance = time_measured * 0.0343 / 2

        gpio.cleanup()
        return distance

    front_distance = measure(PIN.US_SENSOR_FRONT_ECHO)
    right_distance = measure(PIN.US_SENSOR_RIGHT_ECHO)
    left_distance = measure(PIN.US_SENSOR_LEFT_ECHO)

    distances = [front_distance, right_distance, left_distance]

    return distances
