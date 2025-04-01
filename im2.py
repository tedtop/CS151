# Ted Toporkov
# 2024-11-05
# im2.py - Rotates an input image clockwise by 90 degrees

import sys
from picture import Picture
import stddraw

def rotate_image(image_path):

    # Load the image
    picture = Picture(image_path)
    width = picture.width()
    height = picture.height()

    # Create a new picture for the rotated image
    rotated = Picture(height, width)

    # Rotate the image 90 degrees clockwise
    for x in range(width):
        for y in range(height):
            pixel = picture.get(x, y)
            rotated.set(height - 1 - y, x, pixel)

    # Display the rotated image
    stddraw.setCanvasSize(height, width)
    stddraw.picture(rotated)
    stddraw.show()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python im2.py <image_file>")
        sys.exit(1)

    rotate_image(sys.argv[1])