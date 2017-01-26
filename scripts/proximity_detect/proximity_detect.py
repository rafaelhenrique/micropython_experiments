import machine
import time


def run(servo_pin=None, analog_pin=None, red_pin=None, green_pin=None,
        min_position=30, max_position=130, distance_value=600):
    if not servo_pin:
        servo_pin = machine.Pin(12)

    if not analog_pin:
        analog_pin = machine.ADC(0)

    if not red_pin:
        red_pin = machine.Pin(5, machine.Pin.OUT)

    if not green_pin:
        green_pin = machine.Pin(16, machine.Pin.OUT)

    servo = machine.PWM(servo_pin, freq=50)
    while True:
        for position in range(min_position, max_position):
            sensor_value = analog_pin.read()
            if sensor_value <= distance_value:
                print(sensor_value)
                red_pin.high()
                green_pin.low()
            else:
                red_pin.low()
                green_pin.high()

            servo.duty(position)
            time.sleep_ms(100)
        time.sleep(1)

        for position in range(min_position, max_position)[::-1]:
            sensor_value = analog_pin.read()
            if sensor_value <= distance_value:
                print(sensor_value)
                red_pin.high()
                green_pin.low()
            else:
                red_pin.low()
                green_pin.high()

            servo.duty(position)
            time.sleep_ms(100)
        time.sleep(1)
