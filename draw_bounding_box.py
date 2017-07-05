import numpy as np
import cv2
import json
import argparse

parser = argparse.ArgumentParser(description='Draw bounding box around a target')
parser.add_argument('-i', '--image', required=True, help='the image file to load')
args = parser.parse_args()

img = cv2.imread(args.image)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
with open(args.image[:-3] + 'json', 'r') as json_file:
    data = json.load(json_file)
xmin = int(data['xmin'])
ymin = int(data['ymin'])
xmax = int(data['xmax'])
ymax = int(data['ymax'])
cv2.rectangle(img, (xmin, ymin), (xmax, ymax), (255, 0, 0), 2)
cv2.imshow('Display',  img)
cv2.waitKey()
