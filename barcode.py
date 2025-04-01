# Ted Toporkov
# 2024-10-08
# barcode.py - Draw a barcode for a ZIP code

import sys
import stddraw

def draw_bar(x, is_full, bar_width, full_height):
    """Draw a bar at x. Full bars are taller than half bars."""
    if is_full:
        stddraw.filledRectangle(x, 0.0, bar_width, full_height)
    else:
        stddraw.filledRectangle(x, 0.0, bar_width, full_height / 2)

def draw_digit(x, d, bar_width, bar_spacing, full_height):
    """Draw the five bars for a digit starting at position x."""
    codes = [
        "11000", # 0
        "00011", # 1
        "00101", # 2
        "00110", # 3
        "01001", # 4
        "01010", # 5
        "01100", # 6
        "10001", # 7
        "10010", # 8
        "10100"  # 9
    ]

    code = codes[d]

    for i in range(5):
        if code[i] == '1':
            draw_bar(x + i * bar_spacing, True, bar_width, full_height)
        else:
            draw_bar(x + i * bar_spacing, False, bar_width, full_height)
    return x + 5 * bar_spacing

def calculate_checksum(zip_code):
    """Calculate the checksum digit for the ZIP code."""
    return sum(int(c) for c in zip_code if c.isdigit()) % 10

# Get ZIP code from command line
if len(sys.argv) != 2:
    print("Please provide a ZIP code")
    sys.exit()

zip_code = sys.argv[1].strip().replace('-', '')

# Check if ZIP code is valid
if not (len(zip_code) == 5 or len(zip_code) == 9) or not zip_code.isdigit():
    print("ZIP code must be 5 or 9 digits")
    sys.exit()

# Calculate dimensions
num_digits = len(zip_code) + 1  # +1 for checksum
num_bars = num_digits * 5 + 2  # 5 bars per digit, 2 guard rails
bar_width = 1 / (num_bars * 2)  # Each bar and space has equal width
bar_spacing = bar_width * 2

# Setup the drawing window
stddraw.setXscale(0, 1)
stddraw.setYscale(0, 1)

# Calculate checksum
checksum = calculate_checksum(zip_code)

# Set full height for bars
full_height = 0.5

# Draw left guard rail
x = 0
draw_bar(x, True, bar_width, full_height)
x += bar_spacing

# Draw all digits
for c in zip_code:
    x = draw_digit(x, int(c), bar_width, bar_spacing, full_height)

# Draw checksum digit
x = draw_digit(x, checksum, bar_width, bar_spacing, full_height)

# Draw right guard rail
draw_bar(x, True, bar_width, full_height)

# Show the drawing
stddraw.show()