# A collection of steganography tools

- [fixpngsump.py](fixpngsum.py): automatically fix checksums in a PNG file (be aware that **it does not check** the semantic).
- [lsb_detect.py](lsb_detect.py): decompose an image in a layer of bits for a visual detection of LSB steganography.
- [alpha_detect.py](alpha_detect.py): generate an image of the alpha plan (transparency) of another image.
- [alpha_extract.py](alpha_extract.py): extract the alpha plan (transparency) of an image as hexadecimal values.
- [extract_pixel_indicator.py](extract_pixel_indicator.py: extract a message hidden by [the pixel indicator technique](https://www.semanticscholar.org/paper/Pixel-Indicator-Technique-for-RGB-Image-Gutub/b3cd1fd840c74427750b9e1ed1ebed7a8d629cbb?p2df).
