"""
Geometry Calculator Client
Demonstrates usage of the geometry module

Author: Ted Toporkov
Date: October 18, 2024
"""

import stdio
import geometry

def main():
    try:
        # Example 1: Calculate area and perimeter of a rectangle
        length1 = 10
        width1 = 5

        stdio.writeln(f"Rectangle 1: {length1} x {width1}")
        stdio.writeln(f"Area: {geometry.calculate_area(length1, width1):.2f}")
        stdio.writeln(f"Perimeter: {geometry.calculate_perimeter(length1, width1):.2f}")

        # Example 2: Calculate area and perimeter of another rectangle
        length2 = 7.5
        width2 = 3.2

        stdio.writeln("")  # Empty line
        stdio.writeln(f"Rectangle 2: {length2} x {width2}")
        stdio.writeln(f"Area: {geometry.calculate_area(length2, width2):.2f}")
        stdio.writeln(f"Perimeter: {geometry.calculate_perimeter(length2, width2):.2f}")

        # Example 3: Try with invalid input
        stdio.writeln("\nTrying with invalid input:")
        geometry.calculate_area(-2, 4)

    except ValueError as e:
        stdio.writeln(f"Error: {str(e)}")
        return 1

    return 0

if __name__ == "__main__":
    main()

"""
To run this client from the command line:
python geometry_client.py

Requires:
1. stdio.py from Princeton's introcs library to be in the same directory
2. geometry.py to be in the same directory
"""
