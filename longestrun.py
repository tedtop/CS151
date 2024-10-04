# Ted Toporkov
# 2024-09-25
# longestrun.py - find longest number of consecutive ints in a list

import stdio

previous_value = 0
current_run_value = 0
current_run_count = 0
longest_run_value = 0
longest_run_count = 0

while not stdio.isEmpty():
    current_value = stdio.readInt()

    # if the current value is the same as the previous value, increment the current run count
    if previous_value == current_value:
        current_run_value = current_value
        current_run_count += 1
    # if the current value is different from the previous value, reset the current run count
    else:
        current_run_value = current_value
        current_run_count = 1

    # if the current run count is greater than the longest run count, update the longest run count and value
    if current_run_count > longest_run_count:
        longest_run_value = current_run_value
        longest_run_count = current_run_count

    # assign current_value to previous_value for the next iteration
    previous_value = current_value

# print(longest_run_value, longest_run_count)

stdio.writeln('Longest run:  ' + str(longest_run_count) + ' consecutive ' + str(longest_run_value) + 's')