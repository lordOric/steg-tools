#!/usr/bin/env python3

'''
Extract the alpha plan (transparency) of an image as hexadecimal values
'''

# pip install Pillow
from PIL import Image
from os.path import splitext
import sys

if len(sys.argv) != 2:
    print(f'Syntax: {sys.argv[0]} <image>')
    exit(-1)
file_input = sys.argv[1]
filename, extension = splitext(file_input)


input = Image.open(file_input)
width, height = input.size
pixels = input.load()

output = Image.new('RGB', input.size)
new_pixels = output.load()

alpha = list()
for x in range(width):
    for y in range(height):
        _, _, _, a = pixels[x, y]
        alpha.append(a)
alpha = [ f'{a:02x}' for a in alpha]
print(' '.join(alpha))