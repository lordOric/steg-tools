#!/usr/bin/env python3

'''
Remove the alpha channel
'''

# pip install Pillow
from PIL import Image
import sys

if len(sys.argv) != 3:
    print(f'Syntax: {sys.argv[0]} <input> <output>')
    exit(-1)
if sys.argv[1] == '-':
    file_input = sys.stdin.buffer
else:
    file_input = sys.argv[1]
if sys.argv[2] == '-':
    file_output = sys.stdout.buffer
else:
    file_input = sys.argv[2]

Image.open(file_input).convert('RGB').save(file_output, format='png')