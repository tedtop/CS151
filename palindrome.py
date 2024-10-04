# Ted Toporkov
# 9/9/2024
# Palindrome Quiz

import stdio
import sys
import re

string = sys.argv[1]

# Remove non-letter & non-numerical chars, then lowercase the string for comparison
inexact_palindrome = re.sub(r'[^a-zA-Z0-9]', '', string)
inexact_palindrome = inexact_palindrome.lower()

if string == string[::-1]: # test for strict palindrome
    stdio.writeln("This is a palindrome")
elif inexact_palindrome == inexact_palindrome[::-1]: # test for inexact palindrome
    stdio.writeln("This is an inexact palindrome")
else:
    stdio.writeln("Sorry, this is not a palindrome.")