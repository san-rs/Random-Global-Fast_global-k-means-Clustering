import numpy as np
import math
import random
from itertools import repeat

def randomKmeans(samples, k, TOL, C):
	SS_Previous = 0
	samplesLength = len(samples)
	dim = len(samples[0])
	
	while 1:
		P = [[] for i in repeat(None, k)]
		# find the closest cluster centroid
		for i in range(samplesLength):
			minIdx = 0
			minVal = eucliDist(samples[i], C[0], dim)
			for j in range(1,k):
				dist = eucliDist(samples[i], C[j], dim)
				if (dist < minVal):
					minIdx = j
					minVal = dist
			# assign the point to the correct cluster
			P[minIdx].append(samples[i])

		# recalculating cluster centroid
		for j in range(k):
			coords = P[j]
			if(len(coords) == 0):
				coords = random.sample(samples, 1)
			zipped = zip(*coords)
			num = len(coords)
			C[j] = [math.fsum(dList)/num for dList in zipped]
		
		SS_Error = 0
		
		# calculating total clustering error
		for idx in range(k):
			for p_idx in range(len(P[idx])):
				SS_Error += sqEucliDist(P[idx][p_idx], C[idx], dim)

		# check if no change in SSE
		delta = abs(SS_Error - SS_Previous)

		if (delta < TOL):
			break
		
		SS_Previous = SS_Error
		
	return round(SS_Error, 4), C, P

# calculating Euclidean Distance
def eucliDist(sample, center, dim):
	distance = 0
	for x in range(dim):
		distance += pow((sample[x] - center[x]), 2)
	return pow(distance,0.5)

# calculating Squared Euclidean Distance
def sqEucliDist(sample, center, dim):
	sumsq = 0
	for x in range(dim):
		sumsq += pow((sample[x] - center[x]), 2)
	return sumsq
