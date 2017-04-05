from PIL import Image,ImageDraw,ImageFont,ImageColor,ImageOps,ImageFilter
import random as rand
import math
import argparse
import Target
import os
import sys

def get_color():
    '''Generate random color

    Returns:
        color_code: hue, saturation, luminance string
        color: color name string
    '''
    color = rand.choice(list(Target.Color))

    saturation = rand.randint(50, 100)
    luminance = rand.randint(40, 60)

    if color.name == 'red':
        hue = rand.randint(0, 4)
    elif color.name == 'orange':
        hue = rand.randint(9, 33)
    elif color.name == 'yellow':
        hue = rand.randint(43, 55)
    elif color.name == 'green':
        hue = rand.randint(75, 120)
    elif color.name == 'blue':
        hue = rand.randint(200, 233)
    elif color.name == 'purple':
        hue = rand.randint(266, 291)
    elif color.name == 'brown':
        hue = rand.randint(13, 20)
        saturation = rand.randint(25, 50)
        luminance = rand.randint(22, 40)
    elif color.name == 'black':
        hue = rand.randint(0, 360)
        saturation = rand.randint(0, 12)
        luminance = rand.randint(0, 13)
    elif color.name == 'gray':
        hue = rand.randint(0, 360)
        saturation = rand.randint(0, 12)
        luminance = rand.randint(25, 60)
    elif color.name == 'white':
        hue = rand.randint(0, 360)
        saturation = rand.randint(0, 12)
        luminance = rand.randint(80, 100)
    else:
        sys.exit('color not found')
    color_code = 'hsl(%d, %d%%, %d%%)' % (hue, saturation, luminance)
    return color_code, color

def draw_shape(draw, shape, size, color):
    '''Draw random shape

    Args:
        draw: ImageDraw.Draw
        size: max size of target in pixels
        color: hsl color string

    Returns:
        shape: Target.shape
    '''

    if shape.name == 'circle':
        draw_circle(draw, size, color)
    elif shape.name == 'semicircle':
        draw_semicircle(draw, size, color)
    elif shape.name == 'quarter_circle':
        draw_quarter_circle(draw, size, color)
    elif shape.name == 'triangle':
        draw_polygon(draw, size, 3, color)
    elif shape.name == 'square':
        draw_square(draw, size, color)
    elif shape.name == 'rectangle':
        draw_rectangle(draw, size, color)
    elif shape.name == 'trapezoid':
        draw_trapezoid(draw, size, color)
    elif shape.name == 'pentagon':
        draw_polygon(draw, size, 5, color)
    elif shape.name == 'hexagon':
        draw_polygon(draw, size, 6, color)
    elif shape.name == 'heptagon':
        draw_polygon(draw, size, 7, color)
    elif shape.name == 'octagon':
        draw_polygon(draw, size, 8, color)
    elif shape.name == 'star':
        draw_star(draw, size, color)
    elif shape.name == 'cross':
        draw_cross(draw, size, color)
    else:
        sys.exit(shape.name + ' not found')

def draw_circle(draw, size, color):
    square_height = size[0]*rand.randint(60,95)/100
    square_border = (size[0] - square_height)/2
    top=(square_border, square_border)
    bottom=(size[0]-square_border, size[0]-square_border)
    draw.pieslice([top, bottom], 0, 360, fill=color)

def draw_semicircle(draw, size, color):
    square_height = size[0]*rand.randint(85,100)/100
    square_border = (size[0] - square_height)/2
    offset = square_height/4
    top=(square_border, square_border+offset)
    bottom=(size[0]-square_border, size[0]-square_border+offset)
    draw.pieslice([top, bottom], 180, 360, fill=color)

def draw_quarter_circle(draw, size, color):
    square_height = size[0]*rand.randint(140,170)/100
    square_border = (size[0] - square_height)/2
    offset = square_height/4
    top=(square_border+offset, square_border+offset)
    bottom=(size[0]-square_border+offset,
            size[0]-square_border+offset)
    draw.pieslice([top, bottom], 180, 270, fill=color)
    draw.point((0,0), fill=color)
    draw.point((0,0), fill=color)

def draw_square(draw, size, color):
    square_height = size[0]*rand.randint(55,90)/100
    square_border = (size[0] - square_height)/2
    top=(square_border, square_border)
    bottom=(size[0]-square_border, size[0]-square_border)
    draw.rectangle([top, bottom], fill=color)

def draw_rectangle(draw, size, color):
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

def draw_trapezoid(draw, size, color):
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

def draw_star(draw, size, color):
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

def draw_polygon(draw, size, sides, color):
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

def draw_cross(draw, size, color):
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

def draw_text(draw, text, size, color):
    '''Draw random alphanumeric

    Args:
        draw: ImageDraw.Draw
        size: max size of target in pixels
        color: hsl color string

    Returns:
        text: the alphanumeric that was drawn
    '''
    font_location="FreeSansBold.ttf"
    font = ImageFont.truetype(font_location, size=int(size[0]*50/100))
    text_width, text_height = draw.textsize(text, font)
    text_pos = ((size[0]-text_width)/2, (size[1]-text_height)/2)
    draw.text(text_pos, text, fill=color, font=font)

def create_target(size, save_name, shape, character):
    im = Image.new('RGBA', size, color=(0,0,0,0))
    draw = ImageDraw.Draw(im)
    shape_color_code, shape_color = get_color()
    text_color_code, text_color = get_color()
    #Prevent target and letter from being the same color
    while shape_color == text_color:
        shape_color_code, shape_color = get_color()
        text_color_code, text_color = get_color()

    draw_shape(draw, shape, size, shape_color_code)
    draw_text(draw, character, size, text_color_code)
    im = ImageOps.expand(im, border=int(size[0]*10/100), fill=(0))
    orientation=rand.randint(0,355)
    im = im.rotate(orientation)
    im = im.filter(ImageFilter.GaussianBlur(radius=args.blur))

    im = im.convert('RGB')
    del draw # done drawing
    prefix_dir = str(shape.name + '_' + character)
    if not os.path.isdir(prefix_dir):
        os.mkdir(prefix_dir)
    im.save(os.path.join(prefix_dir, save_name + '.png'), 'PNG', quality=100, optimize=True, progressive=True)

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
    for shape in Target.Shape:
        for character in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890':
            for i in range(args.number):
                save_name = "target" + str(i).zfill(8)
                create_target(size, save_name, shape, character)
