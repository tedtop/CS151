# Ted Toporkov
# 2024-09-16
# boysandgirls.py

import sys
import stdio
import stdarray
import random

"""
A couple beginning a family decides to keep having children until they have at least one of either sex.
Estimate the average number of children they will have via simulation. The number of trials is given as
a command-line argument.  Also estimate the most common outcome (record the frequency counts for 2, 3,
and 4 children, and also for 5 and above). Assume that the probability p of having a boy or girl is 1/2.
"""

num_trials = int(sys.argv[1])
freq_map = stdarray.create1D(6,0)
total_children = 0 # across all trials (to calculate avg # of children per trial)

for i in range(0, num_trials):
    boys = 0
    girls = 0
    while (True): # loop until there is at least one boy and one girl
        child = random.choice([0,1]) # select 0.50 boy or girl
        if (child == 0):
            boys = boys + 1 # increment boys if it's a boy
        elif (child == 1):
            girls = girls + 1 # increment girls if it's a girl
        else:
            raise IndexError
        if (boys >= 1 and girls >= 1):
            total_kids_this_trial = boys + girls # total kids produced in this trial
            total_children = total_children + total_kids_this_trial # increment total children across all trials
            if (total_kids_this_trial >= 5): total_kids_this_trial = 5 # truncate the total number of kids in trial
            freq_map[total_kids_this_trial] = freq_map[total_kids_this_trial] + 1 # increment 2|3|4|5+ frequency table
            break

stdio.writeln('Avg # children: ' + str(total_children / num_trials))
stdio.writeln('Trials with 2 children: ' + str(freq_map[2]))
stdio.writeln('Trials with 3 children: ' + str(freq_map[3]))
stdio.writeln('Trials with 4 children: ' + str(freq_map[4]))
stdio.writeln('Trials with 5 or more children: ' + str(freq_map[5]))


"""
 ~/Desktop/CS151/ python boysandgirls.py 1000
Avg # children: 2.981
Trials with 2 children: 513
Trials with 3 children: 250
Trials with 4 children: 100
Trials with 5 or more children: 137
 ~/Desktop/CS151/ python boysandgirls.py 1000
Avg # children: 3.068
Trials with 2 children: 490
Trials with 3 children: 251
Trials with 4 children: 118
Trials with 5 or more children: 141
 ~/Desktop/CS151/ python boysandgirls.py 1000
Avg # children: 2.979
Trials with 2 children: 492
Trials with 3 children: 256
Trials with 4 children: 137
Trials with 5 or more children: 115
 ~/Desktop/CS151/ python boysandgirls.py 1000
Avg # children: 3.025
Trials with 2 children: 488
Trials with 3 children: 256
Trials with 4 children: 139
Trials with 5 or more children: 117
 ~/Desktop/CS151/ python boysandgirls.py 1000
Avg # children: 2.897
Trials with 2 children: 515
Trials with 3 children: 255
Trials with 4 children: 135
Trials with 5 or more children: 95
 ~/Desktop/CS151/ python boysandgirls.py 1000
Avg # children: 3.005
Trials with 2 children: 483
Trials with 3 children: 269
Trials with 4 children: 133
Trials with 5 or more children: 115
 ~/Desktop/CS151/ python boysandgirls.py 1000
Avg # children: 2.957
Trials with 2 children: 508
Trials with 3 children: 254
Trials with 4 children: 121
Trials with 5 or more children: 117
 ~/Desktop/CS151/ python boysandgirls.py 10000
Avg # children: 3.0041
Trials with 2 children: 4970
Trials with 3 children: 2525
Trials with 4 children: 1233
Trials with 5 or more children: 1272
 ~/Desktop/CS151/ python boysandgirls.py 10000
Avg # children: 3.0238
Trials with 2 children: 4955
Trials with 3 children: 2474
Trials with 4 children: 1252
Trials with 5 or more children: 1319
 ~/Desktop/CS151/ python boysandgirls.py 10000
Avg # children: 2.9998
Trials with 2 children: 4980
Trials with 3 children: 2568
Trials with 4 children: 1222
Trials with 5 or more children: 1230
 ~/Desktop/CS151/ python boysandgirls.py 10000
Avg # children: 3.0123
Trials with 2 children: 4926
Trials with 3 children: 2505
Trials with 4 children: 1336
Trials with 5 or more children: 1233
 ~/Desktop/CS151/ python boysandgirls.py 10000
Avg # children: 2.9946
Trials with 2 children: 4968
Trials with 3 children: 2564
Trials with 4 children: 1219
Trials with 5 or more children: 1249
 ~/Desktop/CS151/ python boysandgirls.py 100000
Avg # children: 3.00623
Trials with 2 children: 49831
Trials with 3 children: 25027
Trials with 4 children: 12515
Trials with 5 or more children: 12627
 ~/Desktop/CS151/ python boysandgirls.py 100000
Avg # children: 2.99524
Trials with 2 children: 50163
Trials with 3 children: 24880
Trials with 4 children: 12480
Trials with 5 or more children: 12477
 ~/Desktop/CS151/ python boysandgirls.py 100000
Avg # children: 2.99645
Trials with 2 children: 50214
Trials with 3 children: 24963
Trials with 4 children: 12320
Trials with 5 or more children: 12503
 ~/Desktop/CS151/ python boysandgirls.py 1000000
Avg # children: 2.998359
Trials with 2 children: 500856
Trials with 3 children: 249153
Trials with 4 children: 124803
Trials with 5 or more children: 125188
 ~/Desktop/CS151/ python boysandgirls.py 1000000
Avg # children: 2.999207
Trials with 2 children: 500224
Trials with 3 children: 249682
Trials with 4 children: 125409
Trials with 5 or more children: 124685
 ~/Desktop/CS151/ python boysandgirls.py 1000000
Avg # children: 3.000166
Trials with 2 children: 499581
Trials with 3 children: 250507
Trials with 4 children: 125035
Trials with 5 or more children: 124877
 ~/Desktop/CS151/ python boysandgirls.py 1000000
Avg # children: 3.002092
Trials with 2 children: 499512
Trials with 3 children: 249743
Trials with 4 children: 125704
Trials with 5 or more children: 125041
 ~/Desktop/CS151/ python boysandgirls.py 10000000
Avg # children: 3.0001545
Trials with 2 children: 4999249
Trials with 3 children: 2500232
Trials with 4 children: 1250624
Trials with 5 or more children: 1249895
 ~/Desktop/CS151/ python boysandgirls.py 10000000
Avg # children: 2.9996524
Trials with 2 children: 5000566
Trials with 3 children: 2500913
Trials with 4 children: 1249555
Trials with 5 or more children: 1248966
"""