#!/usr/bin/env python3

'''
Returns the frequency of each color found in an image
'''

# pip install Pillow
from PIL import Image
from os.path import splitext
import sys

if len(sys.argv) != 2:
    print(f'Syntax: {sys.argv[0]} <image>')
    exit(-1)
file_input = sys.argv[1]

input = Image.open(file_input)
width, height = input.size
pixels = input.load()

freq = dict()
for x in range(width):
    for y in range(height):
        r, g, b = pixels[x, y]
        color = f'{r:02x}{g:02x}{b:02x}'
        if color in freq:
            freq[color] += 1
        else:
            freq[color] = 1
freq = sorted(freq.items(), key=lambda x:x[1], reverse=True)

total = width * height
for k, v in freq:
    print(f'#{k} : {v/total*100:.2f}% ({v}/{total})')