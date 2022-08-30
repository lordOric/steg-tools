#!/usr/bin/env python3

from PIL import Image
import sys

if len(sys.argv) < 2 or len(sys.argv) > 3:
    print(f'Syntax: {sys.argv[0]} <image> [R|G|B]')
    print('\tThe second parameter allows to force the indicator channel. Otherwise, it is derived from the length of the message, as stated in the paper.')
    exit(-1)

file_input = sys.argv[1]
ic = None
if len(sys.argv) ==3:
    ic = sys.argv[2]
    print(f'Indicator forced to {ic}')

im = Image.open(file_input)
px = im.load()
width, height =  im.size

def is_prime(n): 
    all(n % i for i in range(2, int(n**0.5)+1)) and n > 1

def chunk_string(string, length):
    return (string[0+i:length+i] for i in range(0, len(string), length))

def parity(bits):
    return bits.count('1') % 2

def transpose(bits, channels):
    if channels == 'RGB':
        return [ bits[0], bits[1], bits[2] ]
    elif channels == 'RBG':
        return [ bits[0], bits[2], bits[1] ]
    elif channels == 'GRB':
        return [ bits[1], bits[0], bits[2] ]
    elif channels == 'GBR':
        return [ bits[1], bits[2], bits[0] ]
    elif channels == 'BRG':
        return [ bits[2], bits[0], bits[1] ]
    elif channels == 'BGR':
        return [ bits[2], bits[1], bits[2] ]

# The length
length = [ f'{x:08b}' for i in range(3) for x in px[i, 0] ][:8]
length = ''.join(length)
par = parity(length)
length = int(length, 2)
print(f'Length: {length}')

# Transpose table
if ic == 'R' or (ic is None and length%2 == 0):
    if parity == 1:
        channels = 'RGB'
    else:
        channels = 'RBG'
elif ic == 'B' or (ic is None and is_prime(length)):
    if parity == 1:
        channels = 'BRG'
    else:
        channels = 'BGR'
else:
    if parity == 1:
        channels = 'GRB'
    else:
        channels = 'GBR'
print(f'Channels: {channels}')

hidden = ''
i = width
while len(hidden) < length:
    x, y = i % width, i // width
    indic, first, second = transpose([x & 3 for x in px[x, y]], channels)
    if indic == 0:
        hidden += ''
    elif indic == 1:
        hidden += f'{second:02b}'
    elif indic == 2:
        hidden += f'{first:02b}'
    else:
        hidden += f'{first:02b}{second:02b}'
    i += 1

plain = ''
for c in chunk_string(hidden, 8):
    c = int(c, 2)
    if c < 32 or c > 127:
        plain += '.'
    else:
        plain += chr(c)
print(f'Message: {plain}')