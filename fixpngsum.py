#!/usr/bin/env python3

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

def handle_chunk(input, output):
    # Chunk length
    l = input.read(4)
    #print(f'Read {l}')
    if l == b'':
        return True # EOF
    l = int.from_bytes(l, "big")

    # Chunk name
    name = input.read(4)
    #print(f'Read {name}')
    real_crc = crc32(name)

    # Chunk data
    data = input.read(l)
    #print(f'Read {data}')
    real_crc = crc32(data, real_crc)

    # Chunk crc
    exp_crc = int.from_bytes(input.read(4), 'big')
    #print(f'Read {exp_crc}')
    
    # Verbose
    print(f'Chunk {name.decode("utf8")} ({l}) : real CRC {real_crc:08x}, expected CRC {exp_crc:08x} => ', end='')
    if real_crc != exp_crc:
        print('fixing...')
    else:
        print('OK !')

    # Write output
    output.write(l.to_bytes(4, 'big'))
    output.write(name)
    output.write(data)
    output.write(real_crc.to_bytes(4, 'big'))

    return False


# Read and fix chunks
eof = False
while not eof:
    eof = handle_chunk(input, output)

# End
print(f'{file_input} has been fixed in {file_output}')
input.close()
output.close()
