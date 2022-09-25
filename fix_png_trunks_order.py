#!/usr/bin/env python3

'''
Automatically reorder the trunks of a PNG accordingly to the standard.
The structure of the PNG must be valid before launching it !
'''

import sys
from zlib import crc32

if len(sys.argv) != 3:
    print(f'Syntax: {sys.argv[0]} <png> <fixed_png>')
    exit(-1)
file_input = sys.argv[1]
file_output = sys.argv[2]

print(f'Fixing {file_input} in {file_output}')
input = open(file_input, 'rb')
output = open(file_output, 'wb')

# Copy signature (8 bytes)
output.write(input.read(8))

def read_chunk(input):
    # Chunk length
    l = input.read(4)
    #print(f'Read {l}')
    if l == b'':
        return False, b'' # EOF
    l = int.from_bytes(l, "big")

    # Chunk name
    name = input.read(4)
    #print(f'Read {name}')
    real_crc = crc32(name)

    # Chunk data
    data = input.read(l)

    # Chunk crc
    exp_crc = int.from_bytes(input.read(4), 'big')
    #print(f'Read {exp_crc}')
    
    return name.decode('utf-8'), data

def write_chunk(output, name, data):
    name = name.encode('utf-8')
    crc = crc32(data, crc32(name))
    output.write(len(data).to_bytes(4, 'big'))
    output.write(name)
    output.write(data)
    output.write(crc.to_bytes(4, 'big'))


# Read chunks
chunks = dict()
while True:
    name, data = read_chunk(input)
    if name == False:
        break
    print(f'Reading {name}')
    if name not in chunks:
        chunks[name] = list()
    chunks[name].append(data)

# Write in the proper order
for chunk_type in ['IHDR', 'iTXt', 'tEXt', 'zTXt', 'tIME', 'gAMA', 'cHRM', 'sRGB', 'iCCP', 'sBIT', 'PLTE', 'hIST', 'tRNS', 'bKGD', 'pHYs', 'sPLT', 'IDAT', 'IEND']:
    if chunk_type not in chunks:
        continue
    for chunk in chunks[chunk_type]:
        print(f'Writing {chunk_type}')
        write_chunk(output, chunk_type, chunk)

# End
print(f'{file_input} has been fixed in {file_output}')
input.close()
output.close()
