import machine
import time


def blink_loop(pin=None):
    if not pin:
        pin = machine.Pin(16, machine.Pin.OUT)  # create output pin on GPIO0

    while True:
        pin.low()  # set pin to low
        time.sleep(3)
        pin.high()  # set pin to high
        time.sleep(3)


def servo_loop(pin=None, min_position=30, max_position=130):
    if not pin:
        pin = machine.Pin(12)

    servo = machine.PWM(pin, freq=50)
    while True:
        for position in range(min_position, max_position):
            servo.duty(position)

        time.sleep(3)

        for position in range(min_position, max_position)[::-1]:
            servo.duty(position)

        time.sleep(3)
