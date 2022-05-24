# Usage python generate-regression-data.py <#SAMPLES> <BIAS> <dist1> <dist2> ...
# Each <dist> looks like <MEAN>,<STD_DEVIATION>,<TARGET_WEIGHT>
# Example: python generate-regression-data.py 20000 3.67,0.46,1 0,10,-300 -53,10.589,0.25
# This example creates 20,000 samples
# 
# Each data sample will have as many features as the number of distributions
# Each feature will be distributed normally by the corresponding feature command line arg
# 
# A file will be created called regression-data.csv and the targets will be the last row 

import sys
import numpy as np

num_samples = int(sys.argv[1])
bias = float(sys.argv[2])
weights = []
distributions = []
dimensions = 0
samples = []

data = []

for arg in sys.argv[3:]:
    params = arg.split(',')
    distributions.append((float(params[0]), float(params[1])))
    weights.append(float(params[2]))
    dimensions += 1

weights = np.array(weights)

for i in range(num_samples):
    sample = []
    for j in range(dimensions):
        number = np.random.normal(distributions[j][0], distributions[j][1], 1)
        sample.append(number[0])
    sample.append(np.dot(weights, sample) + bias)
    sample = np.array(sample)
    samples.append(sample)

samples = np.array(samples)

np.savetxt('regression-data.csv', samples, delimiter=',')