#!/usr/bin/env python3

'''
Extract the LSB of an image and store it in a file
'''

# pip install Pillow
from PIL import Image
from itertools import chain
import sys

if len(sys.argv) != 4:
    print(f'Syntax: {sys.argv[0]} <input> <bit-plan (0-7)> <output>')
    exit(-1)
file_input = sys.argv[1]
bit_plan = int(sys.argv[2])
file_output = sys.argv[3]

input = Image.open(file_input)
data = input.getdata()
data = [y for x in data for y in x]
bits = [ ( x >> bit_plan ) & 1 for x in data ]

content = list()
for i in range(0, len(bits), 8):
    byte = bits[i:i+8]
    byte = sum([byte[b] << (7 - b) for b in range(0, 8)])
    content.append(byte)
open(file_output, 'wb').write(bytes(content))