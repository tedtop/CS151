# Ted Toporkov
# 2024-11-05
# im3.py - Extracts and displays the red, green, and blue components of an image

import sys
from picture import Picture
import stddraw
from color import Color

def extract_components(image_path):

    # Load the image
    picture = Picture(image_path)
    width = picture.width()
    height = picture.height()

    # Create three new pictures for each color component
    red_img = Picture(width, height)
    green_img = Picture(width, height)
    blue_img = Picture(width, height)

    # Process each pixel
    for x in range(width):
        for y in range(height):
            # Get pixel color
            pixel = picture.get(x, y)

            # Extract color components
            red = pixel.getRed()
            green = pixel.getGreen()
            blue = pixel.getBlue()

            # Create color-only pixels
            red_img.set(x, y, Color(red, 0, 0))
            green_img.set(x, y, Color(0, green, 0))
            blue_img.set(x, y, Color(0, 0, blue))

    # Create a new canvas that is three times the width of the original image
    total_width = width * 3
    stddraw.setCanvasSize(total_width, height)

    # Set the scale of the coordinate system
    stddraw.setXscale(0, total_width)
    stddraw.setYscale(0, height)

    # Draw each image in its respective position
    stddraw.picture(red_img, width / 2, height / 2)  # Red on the left
    stddraw.picture(green_img, width * 3 / 2, height / 2)  # Green in the middle
    stddraw.picture(blue_img, width * 5 / 2, height / 2)  # Blue on the right

    stddraw.show()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python im3.py <image_file>")
        sys.exit(1)

    extract_components(sys.argv[1])