from PIL import Image,ImageDraw,ImageFont,ImageColor,ImageOps,ImageFilter
import random as rand
import string
import json
import math
import argparse

class Color:
    def __init__(self):
        self.color_list = ('red',
                            'orange',
                            'yellow',
                            'green',
                            'blue',
                            'purple',
                            'brown',
                            'black',
                            'gray',
                            'white')
        self.text = None
        self.color = None

    def get_color(self):
        self.text = rand.choice(self.color_list)

        saturation = rand.randint(50, 100)
        luminance = rand.randint(40, 60)

        if self.text == 'red':
            hue = rand.randint(0, 4)
        elif self.text == 'orange':
            hue = rand.randint(9, 33)
        elif self.text == 'yellow':
            hue = rand.randint(43, 55)
        elif self.text == 'green':
            hue = rand.randint(75, 120)
        elif self.text == 'blue':
            hue = rand.randint(200, 233)
        elif self.text == 'purple':
            hue = rand.randint(266, 291)
        elif self.text == 'brown':
            hue = rand.randint(13, 20)
            saturation = rand.randint(25, 50)
            luminance = rand.randint(22, 40)
        elif self.text == 'black':
            hue = rand.randint(0, 360)
            saturation = rand.randint(0, 12)
            luminance = rand.randint(0, 13)
        elif self.text == 'gray':
            hue = rand.randint(0, 360)
            saturation = rand.randint(0, 12)
            luminance = rand.randint(25, 60)
        elif self.text == 'white':
            hue = rand.randint(0, 360)
            saturation = rand.randint(0, 12)
            luminance = rand.randint(80, 100)
        self.color = 'hsl(%d, %d%%, %d%%)' % (hue, saturation, luminance)

class Shape:
    def __init__(self):
        self.shape_list = ('circle',
                    'semicircle',
                    'quarter_circle',
                    'triangle',
                    'square',
                    'rectangle',
                    'trapedoid',
                    'pentagon',
                    'hexagon',
                    'heptagon',
                    'octagon',
                    'star',
                    'cross',)
        self.text =None

    def draw_shape(self, draw, size, color, text=None):
        if(text==None):
            self.text = rand.choice(self.shape_list)
        else:
            self.text = text

        if self.text == 'circle':
            self.draw_circle(draw, size, shape_color.color)
        elif self.text == 'semicircle':
            self.draw_semicircle(draw, size, shape_color.color)
        elif self.text == 'quarter_circle':
            self.draw_quarter_circle(draw, size, shape_color.color)
        elif self.text == 'triangle':
            self.draw_polygon(draw, size, 3, shape_color.color)
        elif self.text == 'square':
            self.draw_square(draw, size, shape_color.color)
        elif self.text == 'rectangle':
            self.draw_rectangle(draw, size, shape_color.color)
        elif self.text == 'trapedoid':
            self.draw_trapezoid(draw, size, shape_color.color)
        elif self.text == 'pentagon':
            self.draw_polygon(draw, size, 5, shape_color.color)
        elif self.text == 'hexagon':
            self.draw_polygon(draw, size, 6, shape_color.color)
        elif self.text == 'heptagon':
            self.draw_polygon(draw, size, 7, shape_color.color)
        elif self.text == 'octagon':
            self.draw_polygon(draw, size, 8, shape_color.color)
        elif self.text == 'star':
            self.draw_star(draw, size, shape_color.color)
        elif self.text == 'cross':
            self.draw_cross(draw, size, shape_color.color)


    def draw_circle(self, draw, size, color):
        square_height = size[0]*rand.randint(60,95)/100
        square_border = (size[0] - square_height)/2
        top=(square_border, square_border)
        bottom=(size[0]-square_border, size[0]-square_border)
        draw.pieslice([top, bottom], 0, 360, fill=color)

    def draw_semicircle(self, draw, size, color):
        square_height = size[0]*rand.randint(85,100)/100
        square_border = (size[0] - square_height)/2
        offset = square_height/4
        top=(square_border, square_border+offset)
        bottom=(size[0]-square_border, size[0]-square_border+offset)
        draw.pieslice([top, bottom], 180, 360, fill=color)

    def draw_quarter_circle(self, draw, size, color):
        square_height = size[0]*rand.randint(140,170)/100
        square_border = (size[0] - square_height)/2
        offset = square_height/4
        top=(square_border+offset, square_border+offset)
        bottom=(size[0]-square_border+offset,
                size[0]-square_border+offset)
        draw.pieslice([top, bottom], 180, 270, fill=color)
        draw.point((0,0), fill=color)
        draw.point((0,0), fill=color)

    def draw_square(self, draw, size, color):
        square_height = size[0]*rand.randint(55,90)/100
        square_border = (size[0] - square_height)/2
        top=(square_border, square_border)
        bottom=(size[0]-square_border, size[0]-square_border)
        draw.rectangle([top, bottom], fill=color)

    def draw_rectangle(self, draw, size, color):
        if(rand.randint(0,1)==0):
            rectangle_width = size[0]*rand.randint(40,50)/100
            rectangle_height = size[0]*rand.randint(80,97)/100
        else:
            rectangle_width = size[0]*rand.randint(80,97)/100
            rectangle_height = size[0]*rand.randint(40,50)/100

        border_width = (size[0] - rectangle_width)/2
        border_height = (size[0] - rectangle_height)/2
        top=(border_width, border_height)
        bottom=(size[0]-border_width, size[0]-border_height)
        draw.rectangle([top, bottom], fill=color)

    def draw_trapezoid(self, draw, size, color):
        top_width = size[0]*rand.randint(40,50)/100
        bottom_width = size[0]*rand.randint(75,95)/100
        height = size[0]*rand.randint(42,60)/100

        border_top_width = (size[0] - top_width)/2
        border_bottom_width = (size[0] - bottom_width)/2
        border_height = (size[0] - height)/2

        top_left=(border_top_width, border_height)
        top_right=(size[0]-border_top_width, border_height)

        bottom_left=(border_bottom_width,
                        size[0]-border_height)

        bottom_right=(size[0]-border_bottom_width,
                        size[0]-border_height)
        draw.polygon((top_left,
                        top_right,
                        bottom_right,
                        bottom_left),
                        fill=color)

    def draw_star(self, draw, size, color):
        sides = 5
        cord = size[0]*55/100
        angle = 2*math.pi/sides
        rotation = math.pi/2
        points =[]
        for s in (0,2,4,1,3):
            points.append(math.cos(angle*s-rotation)*cord+size[0]/2)
            points.append(math.sin(angle*s-rotation)*cord+size[0]/2)
        draw.polygon(points, fill=color)

        #fill in the center pentagon
        rotation = math.pi*3/2
        cord = size[0]*23/100
        points =[]
        for s in range(sides):
            points.append(math.cos(angle*s-rotation)*cord+size[0]/2)
            points.append(math.sin(angle*s-rotation)*cord+size[0]/2)
        draw.polygon(points, fill=color)

    def draw_polygon(self, draw, size, sides, color):
        cord = size[0]*rand.randint(45,50)/100
        angle = 2*math.pi/sides
        rotation = 0
        points =[]
        if(sides % 2 == 1):
            rotation = math.pi/2
        for s in range(sides):
            points.append(math.cos(angle*s-rotation)*cord+size[0]/2)
            points.append(math.sin(angle*s-rotation)*cord+size[0]/2)
        draw.polygon(points, fill=color)

    def draw_cross(self, draw, size, color):
        rectangle_width = size[0]*rand.randint(35,40)/100
        rectangle_height = size[0]*rand.randint(85,99)/100

        border_width = (size[0] - rectangle_width)/2
        border_height = (size[0] - rectangle_height)/2
        top=(border_width, border_height)
        bottom=(size[0]-border_width, size[0]-border_height)
        draw.rectangle([top, bottom], fill=color)
        # draw rectanle turned
        top=(border_height, border_width)
        bottom=(size[0]-border_height, size[0]-border_width)
        draw.rectangle([top, bottom], fill=color)

def draw_text(draw, size, color):
    font_location="FreeSansBold.ttf"
    font = ImageFont.truetype(font_location, size=(size[0]*50/100))
    text = rand.choice(string.ascii_uppercase)
    text_width, text_height = draw.textsize(text, font)
    text_pos = ((size[0]-text_width)/2, (size[1]-text_height)/2)
    draw.text(text_pos, text, fill=text_color.color, font=font)
    return text

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description = 'generate targets')

    parser.add_argument('-s', '--size', type=int, default = 50,
            help='max size in pixels of target')

    parser.add_argument('-n', '--number', type=int, default = 1,
            help='number of targets to generate')

    parser.add_argument('-b', '--blur', type=int, default = 1,
            help='gaussian blur pixel radius')

    args = parser.parse_args()
    size = (args.size, args.size)
    for n in range(args.number):
        im = Image.new('RGBA', size, color=(0,0,0,0))
        draw = ImageDraw.Draw(im)

        shape_color = Color()
        shape_color.get_color()
        text_color = Color()
        text_color.get_color()
        shape = Shape()
        shape.draw_shape(draw, size, shape_color.color)
        text = draw_text(draw, size, text_color.color)
        im = ImageOps.expand(im, border=5, fill=(0))
        orientation=rand.randint(0,355)
        im = im.rotate(orientation)
        im = im.filter(ImageFilter.GaussianBlur(radius=args.blur))

        del draw # done drawing
        save_name = "target" + str(n).zfill(6)
        im.save(save_name + '.png', 'PNG')

        with open(save_name + '.json', 'w') as outfile:
            json.dump({'shape':shape.text,
                        'background_color':shape_color.text,
                        'alphanumeric':text,
                        'alphanumeric_color':text_color.text,
                        'orientation':orientation},
                        outfile,
                        indent=4)
