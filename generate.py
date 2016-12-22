from PIL import Image, ImageDraw, ImageFont
import random
import string

size = (50, 50)
im = Image.new('RGB', size)
draw = ImageDraw.Draw(im)

red = (255,0,0)
text_pos = (size[0]*3/10, size[1]*3/10)
font_location="FreeSansBold.ttf"
font = ImageFont.truetype(font_location, size=(size[0]*4/10))
text = random.choice(string.ascii_uppercase)
draw.text(text_pos, text, fill=red, font=font)

del draw # done drawing

im.save("target.jpg", 'JPEG')

def draw_square(im, draw, size):
    top=(size[0]*1/10, size[0]*1/10
    
