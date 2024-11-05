from hal import hal_led as led
from time import sleep
from hal import hal_input_switch as switch

led.init()
switch.init()

while True:

    sw_value=switch.read_slide_switch()

    if sw_value == 0:
        led.set_output(0, 1)  # Turn LED on
        sleep(0.2)
        led.set_output(0, 0)  # Turn LED off
        sleep(0.2)
    else:
        led.set_output(0, 1)  # Turn LED on
        sleep(0.1)
        led.set_output(0, 0)  # Turn LED off
        sleep(0.1)
