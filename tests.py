''' The main goal of the script is to unsure all the hardware parts are properly working ... ''' 
from gpiozero import RotaryEncoder, Button
from gpiozero.tools import scaled_half
import os
import sys
import time
import RPi.GPIO as GPIO
from utils import Encoder
from board import SCL, SDA
import busio
from PIL import Image, ImageDraw, ImageFont
import adafruit_ssd1306

def test_pi():
    if os.uname().machine == "armv6l":
        print("This is a raspberrypi, test passed !")
        return 1
    else:
        sys.exit("This device isn't a raspberrypi")
           

def valueChanged(value):
    print(f"* New value: {value}")

def test_encoder():
    rotor = RotaryEncoder(a=17, b=6, max_steps=10)
    button = Button(15)
    print(" Press the button : ")   
    button.wait_for_press()
    print(" Rotate the rotor : ")
    rotor.wait_for_rotate()

def test_screen():
    # Create the I2C interface.
    i2c = busio.I2C(SCL, SDA)

    # Create the SSD1306 OLED class.
    # The first two parameters are the pixel width and pixel height.  Change these
    # to the right size for your display!
    disp = adafruit_ssd1306.SSD1306_I2C(128, 32, i2c)
    # Clear display.
    disp.fill(0)
    disp.show()

    # Create blank image for drawing.
    # Make sure to create image with mode '1' for 1-bit color.
    width = disp.width
    height = disp.height
    image = Image.new('1', (width, height))

    # Get drawing object to draw on image.
    draw = ImageDraw.Draw(image)

    # Draw a black filled box to clear the image.
    draw.rectangle((0, 0, width, height), outline=0, fill=0)
    # Draw some shapes.
    # First define some constants to allow easy resizing of shapes.
    padding = -2
    top = padding
    bottom = height-padding
    # Move left to right keeping track of the current x position for drawing shapes.
    x = 0


    # Load default font.
    font = ImageFont.load_default()

    # Alternatively load a TTF font.  Make sure the .ttf font file is in the
    # same directory as the python script!
    # Some other nice fonts to try: http://www.dafont.com/bitmap.php
    #font = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', 9)
    draw.text((x, top+0), "Tests", font=font, fill=255)
    disp.image(image)
    disp.show()
    time.sleep(2)
    draw.rectangle((0, 0, width, height), outline=0, fill=0)

def test_battery():
    pass


test_pi()
test_screen()
test_encoder()
test_battery()