from machine import Pin
import utime

pir = Pin(2, Pin.IN)

led0 = Pin(6, Pin.OUT)
led1 = Pin(7, Pin.OUT)
led2 = Pin(16, Pin.OUT)
led3 = Pin(17, Pin.OUT)

def leds_on (value):
    if value == True:
        led0.low()
        led1.low()
        led2.low()
        led3.low()
    else:
        led0.high()
        led1.high()
        led2.high()
        led3.high()

while True:
    if (pir.value() == 1):
        print ("Turning LEDs on")
        leds_on(True)
        utime.sleep (10)
    else:
        print ("Turning LEDs off")
        leds_on(False)
        utime.sleep (1)


