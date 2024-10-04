# Ted Toporkov
# 2024-09-25
# tenperline.py - prints 10 ints per line

import stdio

count = 1 # start count at 1 so it's not divisible by 10 on first iteration
while stdio.isEmpty() == False: # read until nothing left to read from stdin
    value = stdio.readInt()
    stdio.writef('%5d', value) # write out the value right-aligned in 5 char cell
    if (count % 10 == 0): # insert a newline after very 10 values
        stdio.writeln()
    count += 1