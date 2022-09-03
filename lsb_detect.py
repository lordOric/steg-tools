#!/usr/bin/env python3

'''
Detect LSB by decomposing an RGB image in layers. The result is 8 images,
each one reflecting the value of a bit of the colors.
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

def extract_lsb(size, pixels, bit):
    width, height = size

    output = Image.new('RGB', size)
    new_pixels = output.load()

    for x in range(width):
        for y in range(height):
            r, g, b = pixels[x, y]
            nr, ng, nb = [ ( (x >> bit) & 1 ) * 255 for x in (r, g, b) ]
            new_pixels[x, y] = (nr, ng, nb)
    
    return output

input = Image.open(file_input)
size = input.size
pixels = input.load()

for bit in range(8):
    file_output = f'{filename}_bit{bit}{extension}'
    print(f'Extracting bit {bit} in {file_output}')
    output = extract_lsb(size, pixels, bit)
    output.save(file_output)