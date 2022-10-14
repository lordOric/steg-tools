#!/usr/bin/env python3

'''
Automatically extract the padding of each line of a BMP
'''

import sys

if len(sys.argv) != 2:
    print(f'Syntax: {sys.argv[0]} <bmp>')
    exit(-1)
file_input = sys.argv[1]
input = open(file_input, 'rb')

magic = input.read(2)
if magic != b'BM':
    print(f'{file_input} does not seem to be a BMP.')
    exit(-1)

file_size = int.from_bytes(input.read(4), byteorder='little')
reserved = input.read(4)
data_start = int.from_bytes(input.read(4), byteorder='little')
header_size = int.from_bytes(input.read(4), byteorder='little')
width = int.from_bytes(input.read(4), byteorder='little')
height = int.from_bytes(input.read(4), byteorder='little')
print(f'Size: {width}x{height}')

# Assuming this is a 24 bpp for now...
# (cause the challenge I'm working on is :) )
padding_size = 4 - ( width * 3 ) % 4
print(f'Padding size : {padding_size}')

# Reading the image
content = bytearray()
input.seek(data_start)
for _ in range(height):
    input.read(width*3)
    part = input.read(padding_size)
    content += part
print(content)