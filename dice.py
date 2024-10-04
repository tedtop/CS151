# Ted Toporkov
# 2024-09-20
# dice.py - computes the exact probability distribution for the sum of two dice

import sys
import stdio
import stdarray
import random

def exact_probabilities():
    probabilities = stdarray.create1D(13, 0.0)
    for i in range(1, 7):
        for j in range(1, 7):
            probabilities[i+j] += 1.0
    for k in range(2, 13):
        probabilities[k] /= 36.0
    return probabilities

def simulate_probabilities(trials):
    probabilities = stdarray.create1D(13, 0.0)

    # simulate rolling two dice 'trials' number of times
    for _ in range(trials):
        # Roll two dice and sum their values
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        roll_sum = die1 + die2

        # increment the count for this sum
        probabilities[roll_sum] += 1

    # convert counts to probabilities
    for k in range(2, 13):  # We only care about sums from 2 to 12
        probabilities[k] = probabilities[k] / trials

    return probabilities

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python dice.py <number_of_trials>")
        sys.exit(1)

    trials = int(sys.argv[1])
    simulated_probs = simulate_probabilities(trials)
    exact_probs = exact_probabilities()

    stdio.writeln("Exact results")
    for i in range(2, 13):
        stdio.writeln("Probability the sum of die is " + str(i) + ": " + str(exact_probs[i]))

    stdio.writeln()

    stdio.writeln("Empirical results")
    for i in range(2, 13):
        stdio.writeln("Results the sum of die is " + str(i) + ": " + str(simulated_probs[i]))

    stdio.writeln()

    stdio.writeln("Difference")
    for i in range(2, 13):
        stdio.writeln("Difference when sum is " + str(i) + ": " + str(simulated_probs[i] - exact_probs[i]))

"""
How large does n have to be before your empirical results match the exact results to three decimal places?

Response: 100,000 is the least number of trials needed for the calculated and simulated results to equal to within 3 decimal places.
However, this gives some anomalies with rounding depending on each execution, so the the better number of trials is 1,000,000.

>>> python dice.py 100000
Exact results
Probability the sum of die is 2: 0.027777777777777776
Probability the sum of die is 3: 0.05555555555555555
Probability the sum of die is 4: 0.08333333333333333
Probability the sum of die is 5: 0.1111111111111111
Probability the sum of die is 6: 0.1388888888888889
Probability the sum of die is 7: 0.16666666666666666
Probability the sum of die is 8: 0.1388888888888889
Probability the sum of die is 9: 0.1111111111111111
Probability the sum of die is 10: 0.08333333333333333
Probability the sum of die is 11: 0.05555555555555555
Probability the sum of die is 12: 0.027777777777777776

Empirical results
Results the sum of die is 2: 0.02762
Results the sum of die is 3: 0.05584
Results the sum of die is 4: 0.08397
Results the sum of die is 5: 0.11017
Results the sum of die is 6: 0.13804
Results the sum of die is 7: 0.16712
Results the sum of die is 8: 0.13876
Results the sum of die is 9: 0.11149
Results the sum of die is 10: 0.08296
Results the sum of die is 11: 0.05544
Results the sum of die is 12: 0.02859

Difference
Difference when sum is 2: -0.00015777777777777752
Difference when sum is 3: 0.0002844444444444483
Difference when sum is 4: 0.0006366666666666743
Difference when sum is 5: -0.0009411111111111009
Difference when sum is 6: -0.000848888888888899
Difference when sum is 7: 0.00045333333333333337
Difference when sum is 8: -0.0001288888888889006
Difference when sum is 9: 0.0003788888888889008
Difference when sum is 10: -0.00037333333333332275
Difference when sum is 11: -0.0001155555555555493
Difference when sum is 12: 0.0008122222222222246
"""