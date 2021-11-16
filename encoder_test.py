from RPi import GPIO
from time import sleep




def button_callback(channel):
    print("Button pressed")


clk = 17
dt = 18
btn = 15

GPIO.setmode(GPIO.BCM)
GPIO.setup(clk, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(dt, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(btn, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.add_event_detect(15,GPIO.RISING,callback=button_callback)
counter = 0
clkLastState = GPIO.input(clk)

try:

    while True:
        clkState = GPIO.input(clk)
        dtState = GPIO.input(dt)
        if clkState != clkLastState:
            if dtState != clkState:
                counter += 1
            else:
                counter -= 1
            print(counter)
            clkLastState = clkState
            sleep(0.01)
finally:
        GPIO.cleanup()