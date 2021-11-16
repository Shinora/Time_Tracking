''' The main goal of the script is to unsure all the hardware parts are properly working ... ''' 
from gpiozero import RotaryEncoder
from gpiozero.tools import scaled_half
import os

def test_pi():
    pass

def test_encoder():
    rotor = RotaryEncoder(21, 20)
    rotor.wait_for_active()

def test_screen():
    pass

def test_battery():
    pass


test_pi()
test_encoder()
test_screen()
test_battery()