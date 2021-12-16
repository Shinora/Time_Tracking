import RPi.GPIO as GPIO
import RPi.GPIO as GPIO
from board import SCL, SDA
import busio
import time
import sys
from PIL import Image, ImageDraw, ImageFont
import adafruit_ssd1306

class Activity:
    name = ""
    category = ""
    code = ""
    duration = 0.5
    description = ""
    value = 0

    def __init__(self, name, category, code, duration, description, value):
        self.name = name
        self.category = category
        self.code = code
        self.duration = duration
        self.description = description
        self.value = value


class Question:
    code = ""
    question = ""
    anwsers =  []

    def __init__(self, code, question, anwsers):
        self.code = code
        self.question = question
        self.anwsers = anwsers


class Machine_State():
    current_date = 0
    date_last_record = 0
    hour_last_record = 0
    

    def __init__(self, date, date_last_record, hour_last_record):
        self.current_date = date
        self.date_last_record = date_last_record
        self.hour_last_record = hour_last_record


class Screen():
    # Create the I2C interface.
    i2c = busio.I2C(SCL, SDA)
    # Create the SSD1306 OLED class.
    # The first two parameters are the pixel width and pixel height.  Change these
    # to the right size for your display!
    disp = adafruit_ssd1306.SSD1306_I2C(128, 32, i2c)

    def __init__(self):
    # Clear display.
        self.disp.fill(0)
        self.disp.show()

    # Create blank image for drawing.
    # Make sure to create image with mode '1' for 1-bit color.
        self.width = self.disp.width
        self.height = self.disp.height
        self.image = Image.new('1', (self.width, self.height))

    # Get drawing object to draw on image.
        self.draw = ImageDraw.Draw(self.image)

    # Draw a black filled box to clear the image.
        self.draw.rectangle((0, 0, self.width, self.height), outline=0, fill=0)
    # Draw some shapes.
    # First define some constants to allow easy resizing of shapes.
        self.padding = -2
        self.top = self.padding
        self.bottom = self.height-self.padding
    # Move left to right keeping track of the current x position for drawing shapes.
        self.x = 0

    # Load default font.
        self.font = ImageFont.load_default()
        self.specialfont = ImageFont.truetype("Retron2000.ttf", 15)
    # Alternatively load a TTF font.  Make sure the .ttf font file is in the
    # same directory as the python script!
    # Some other nice fonts to try: http://www.dafont.com/bitmap.php
    #font = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', 9)

    def write(self, text):
        self.clear()
        self.draw.text((self.x, self.top+0), text, font=self.specialfont, fill=255)
        self.disp.image(self.image)
        self.disp.show()

    def clear(self):
        self.draw.rectangle((0, 0, self.width, self.height), outline=0, fill=0)

    def idle(self):
        clock = """
         .--.
    .-._;.--.;_.-.
   (_.'_..--.._'._)
    /.' . 60 . '.\'
   // .      / . \\
  |; .      /   . |;
  ||45    ()    15||
  |; .          . |;
   \\ .        . //
    \'._' 30 '_.'/
     '-._'--'_.-'
         `""` """
        self.write(clock)
