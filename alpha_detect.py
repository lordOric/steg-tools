#!/usr/bin/env python3

'''
Generate an image of the alpha plan (transparency) of another image
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

for x in range(width):
    for y in range(height):
        _, _, _, a = pixels[x, y]
        new_pixels[x, y] = (a*255, a*255, a*255)


file_output = f'{filename}_alpha.{extension}'
print(f'Saving result in {file_output}')
output.save(file_output)