#!/usr/bin/env python3

'''
Extracting colors as hexa
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

for y in range(height):
    for x in range(width):
        colors = pixels[x, y]
        print(f'{colors[0]:02x} {colors[1]:02x} {colors[2]:02x} ', end='')
    print()