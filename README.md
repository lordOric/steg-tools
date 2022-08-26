# Fix sum PNG

This small tool automatically fixes checksums in a PNG file (be aware that **it does not check** the semantic).

Example:
```
$ ./fixsumpng.py test.png fixed.png
Fixing test.png in fixed.png
Chunk IHDR (13) : real CRC f478d4fa, expected CRC f478d4fa => OK !
Chunk acTL (8) : real CRC 71dd04a1, expected CRC 71dd04a1 => OK !
Chunk fcTL (26) : real CRC 8ac08d97, expected CRC 601309ce => fixing...
Chunk IDAT (32768) : real CRC db48c646, expected CRC db48c646 => OK !
Chunk IDAT (9612) : real CRC bf781d70, expected CRC bf781d70 => OK !
Chunk fcTL (26) : real CRC 525e4876, expected CRC f23dd48e => fixing...
Chunk fdAT (32772) : real CRC fb7dde6c, expected CRC fb7dde6c => OK !
Chunk fdAT (32420) : real CRC e1057c91, expected CRC e1057c91 => OK !
Chunk fcTL (26) : real CRC 7a136d70, expected CRC 22e03539 => fixing...
[...]
Chunk IEND (0) : real CRC ae426082, expected CRC ae426082 => OK !
test.png has been fixed in fixed.png
```
