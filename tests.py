''' The main goal of the script is to unsure all the hardware parts are properly working ... ''' 
from gpiozero import RotaryEncoder
from gpiozero.tools import scaled_half
import os
import time
from board import SCL, SDA
import busio
from PIL import Image, ImageDraw, ImageFont
import adafruit_ssd1306

def test_pi():
    print(os.uname().sysname)
    

def test_encoder():
    rotor = RotaryEncoder(21, 20)
    rotor.wait_for_active()

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
    time.sleep(2)

def test_battery():
    print("testing battery")


test_pi()
test_screen()
test_encoder()

test_battery()