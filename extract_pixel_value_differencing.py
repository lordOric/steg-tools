#!/usr/bin/env python3

from math import floor, log, log2
from PIL import Image
import sys

if len(sys.argv) !=2:
    print(f'Syntax: {sys.argv[0]} <image>')
    exit(-1)

file_input = sys.argv[1]
im = Image.open(file_input)
px = im.load()
width, height =  im.size

# Based on "A steganographic method for images by pixel-value differencing"
# ( Da-Chun Wu, Wen-Hsiang Tsai)
# https://people.cs.nctu.edu.tw/~whtsai/Journal%20Paper%20PDFs/Wu_&_Tsai_PRL_2003.pdf
def extract_lsb(d):
    if 0 <= d <= 7:
        return 3
    elif 8 <= d <= 15:
        return 3
    elif 16 <= d <= 31:
        return 4
    elif 32 <= d <= 63:
        return 5
    elif 64 <= d <= 127:
        return 6
    elif 128 <= d <= 255:
        return 7  
 
    raise AssertionError(f'No range found for {d=}')

# Scan the image in zigzag
def get_pixel(i):
    y = i // width
    if y % 2 == 0:
        x = i % width
    else:
        x = width - 1 - (i % width)
    return px[x, y]

def chunk_string(string, length):
    return (string[0+i:length+i] for i in range(0, len(string), length))

# Extraction
i = 0
bits = ''
while i < (width*height):
    p1, p2 = get_pixel(i), get_pixel(i+1)
    d = abs(p2 - p1)
    m = extract_lsb(d)
    lsb = d % (2 ** m)
    lsb = f'{lsb:b}'
    lsb = '0' * (m - len(lsb)) + lsb
    bits += lsb
    i += 2

# Convert to ASCII
plain = ''
for c in chunk_string(bits, 8):
    c = int(c, 2)
    if c < 32 or c > 127:
        plain += '.'
    else:
        plain += chr(c)
print(f'Message: {plain}')