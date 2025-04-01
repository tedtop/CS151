"""
Geometry Calculator Module
Provides functions for calculating properties of rectangles

This module contains functions for:
- Calculating rectangle area
- Calculating rectangle perimeter


Author: Ted Toporkov
Date: October 18, 2024
"""

import stdio

def calculate_area(length, width):
    """
    Calculate the area of a rectangle.

    Args:
        length (float): The length of the rectangle
        width (float): The width of the rectangle

    Returns:
        float: The area of the rectangle
    """
    return _validate_and_multiply(length, width)

def calculate_perimeter(length, width):
    """
    Calculate the perimeter of a rectangle.

    Args:
        length (float): The length of the rectangle
        width (float): The width of the rectangle

    Returns:
        float: The perimeter of the rectangle
    """
    return _validate_and_multiply(length + width, 2)

def _validate_and_multiply(a, b):
    """
    Helper function to validate inputs and perform multiplication.
    Not meant to be called directly by clients.

    Args:
        a (float): First number
        b (float): Second number

    Returns:
        float: Product of the two numbers

    Raises:
        ValueError: If inputs are negative
    """
    if a < 0 or b < 0:
        raise ValueError("Measurements cannot be negative")
    return a * b

# Test client
if __name__ == "__main__":
    # Test cases
    stdio.writeln("Running test cases...")

    # Test case 1: Normal values
    test_length = 5
    test_width = 3
    stdio.writeln(f"Rectangle {test_length} x {test_width}:")
    stdio.writeln(f"Area: {calculate_area(test_length, test_width):.2f}")
    stdio.writeln(f"Perimeter: {calculate_perimeter(test_length, test_width):.2f}")

    # Test case 2: Square (equal sides)
    test_square = 4
    stdio.writeln("")  # Empty line
    stdio.writeln(f"Square {test_square} x {test_square}:")
    stdio.writeln(f"Area: {calculate_area(test_square, test_square):.2f}")
    stdio.writeln(f"Perimeter: {calculate_perimeter(test_square, test_square):.2f}")

    # Test with invalid input
    try:
        stdio.writeln("\nTesting invalid input:")
        calculate_area(-1, 5)
    except ValueError as e:
        stdio.writeln(f"Error caught successfully: {str(e)}")

"""
To run this module directly from the command line:
python geometry.py

Requires stdio.py from Princeton's introcs library to be in the same directory.
This will execute the test cases defined in the __main__ block.
"""
