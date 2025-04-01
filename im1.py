# Ted Toporkov
# 2024-11-05
# im1.py - Creates a histogram of grayscale intensities from an input image

import sys
from picture import Picture
import stddraw
import luminance

def create_histogram(image_path):

    # Load the image
    picture = Picture(image_path)
    width = picture.width()
    height = picture.height()

    # Convert the image to grayscale
    for x in range(width):
        for y in range(height):
            pixel = picture.get(x, y)
            gray = luminance.toGray(pixel)
            picture.set(x, y, gray)

    # Initialize histogram array for 256 intensity values
    histogram = [0] * 256

    # Count frequency of each intensity
    for x in range(width):
        for y in range(height):
            # Get pixel intensity
            intensity = int(picture.get(x, y).getBlue())
            histogram[intensity] += 1

    # Normalize histogram
    max_freq = max(histogram)
    normalized = [h / max_freq for h in histogram]

    # Draw histogram
    stddraw.setXscale(0, 256)
    stddraw.setYscale(0, 1.1)

    # Draw bars
    for i in range(256):
        stddraw.line(i, 0, i, normalized[i])

    # Show the plot
    stddraw.show()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python im1.py <image_file>")
        sys.exit(1)

    create_histogram(sys.argv[1])
