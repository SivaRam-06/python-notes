# file_handling/08_binary_files.py
"""
BINARY FILES
============

What is it?
-----------
Binary files store data in binary format (0s and 1s) rather than text.

When to use it?
---------------
Use binary files when you need to:
1. Store non-text data (images, audio, video)
2. Work with proprietary file formats
3. Save memory-efficient data structures

How to identify it?
-------------------
Look for 'b' mode in open() function and byte data.
"""

# Example 1: Writing binary files
print("=== WRITING BINARY FILES ===")

# Binary data (bytes)
data = b"Binary data here\x00\x01\x02\x03"

# Write to binary file
with open("binary_data.bin", "wb") as file:
    file.write(data)
    print("Binary file created")

# Example 2: Reading binary files
print("\n=== READING BINARY FILES ===")

# Read from binary file
with open("binary_data.bin", "rb") as file:
    binary_content = file.read()
    print(f"Binary content: {binary_content}")
    print(f"Length: {len(binary_content)} bytes")

# Example 3: Working with different data types
print("\n=== WORKING WITH DIFFERENT DATA TYPES ===")

import struct

# Pack different data types into binary format
# Format string: 'i' for integer, 'f' for float, '10s' for 10-character string
packed_data = struct.pack('if10s', 42, 3.14, b'Hello')

# Write packed data
with open("structured_data.bin", "wb") as file:
    file.write(packed_data)
    print("Structured binary file created")

# Read and unpack data
with open("structured_data.bin", "rb") as file:
    data = file.read()
    unpacked_data = struct.unpack('if10s', data)
    print(f"Unpacked data: {unpacked_data}")
    print(f"Integer: {unpacked_data[0]}")
    print(f"Float: {unpacked_data[1]}")
    print(f"String: {unpacked_data[2].decode().strip()}")

# Example 4: Practical example - image processing
print("\n=== PRACTICAL EXAMPLE - IMAGE PROCESSING ===")

# Create a simple BMP file header (simplified)
bmp_header = bytes([
    0x42, 0x4D,             # BM signature
    0x1A, 0x00, 0x00, 0x00, # File size (26 bytes)
    0x00, 0x00,             # Reserved
    0x00, 0x00,             # Reserved
    0x1A, 0x00, 0x00, 0x00, # Offset to pixel data
    0x0C, 0x00, 0x00, 0x00, # Header size
    0x01, 0x00,             # Width (1 pixel)
    0x01, 0x00,             # Height (1 pixel)
    0x01, 0x00,             # Planes
    0x18, 0x00,             # Bits per pixel (24)
    0x00, 0x00, 0x00, 0x00  # No compression
])

# Pixel data (blue pixel)
pixel_data = bytes([0xFF, 0x00, 0x00])  # BGR format

# Write BMP file
with open("blue_pixel.bmp", "wb") as file:
    file.write(bmp_header)
    file.write(pixel_data)
    print("BMP file created")

# Example 5: Reading and modifying binary data
print("\n=== READING AND MODIFYING BINARY DATA ===")

# Read the BMP file
with open("blue_pixel.bmp", "rb") as file:
    content = file.read()
    print(f"File size: {len(content)} bytes")

# Change the pixel color to green
# Pixel data starts at offset 26, change from blue to green
modified_content = bytearray(content)
modified_content[26] = 0x00  # Blue channel
modified_content[27] = 0xFF  # Green channel
modified_content[28] = 0x00  # Red channel

# Write modified BMP
with open("green_pixel.bmp", "wb") as file:
    file.write(modified_content)
    print("Modified BMP file created")

"""
Key Points:
- Use 'b' mode for binary files
- Binary files work with bytes instead of strings
- struct.pack() converts Python values to binary
- struct.unpack() converts binary to Python values
- Binary files are used for non-text data like images
"""
