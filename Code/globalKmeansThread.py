import numpy as np
import math
from threading import Thread

import randomKmeans

globalDictionary = {}

def globalKmeansThread(samples, k, tolerance):
	global globalDictionary
	tempCLusterList = []
	tempCLusterList.append(np.array(samples[0]));	 
	curClustError, centroid, clusterList = randomKmeans.randomKmeans(samples, 1, tolerance, tempCLusterList)
	centroidList = []
	centroidList.append(np.array(centroid[0]))
	prevClustError = curClustError
		
	# run k means for each cluster
	for kVal in range(2, k+1):
		#print "Working on cluster : " + str(kVal)
		globalDictionary = {}
		threads = []
		count = 0

		# use multi threading to speed up the process as the computational complexity is really high
		while(count < len(samples)):
			start = count;
			end = count + (len(samples) / 10)
			t = Thread(target = globalThread, args = (start, end, samples, kVal, tolerance, centroidList,))
			t.start()
			threads.append(t)
			count = end;

		for t in threads:
			t.join()	
			
		# find the centroid with least clustering error
		for key in globalDictionary.keys():
			if key < prevClustError:
				prevClustError = key
				newCentroid = globalDictionary[key]
			
		centroidList = []
		for index in range(0, kVal):
			centroidList.append(np.array(newCentroid[index]))
			
	return round(prevClustError, 4), centroidList

# thread to calculate kmeans for samples from index start to end
def globalThread(start, end , samples, kVal, tolerance, centroidList):
	global globalDictionary
	for i in range(start,end):
		tempCLusterList = []
		tempCLusterList.extend(centroidList)
		tempCLusterList.append(np.array(samples[i]));
		curClustError, centroid, clusterList = randomKmeans.randomKmeans(samples, kVal, tolerance, tempCLusterList)
		globalDictionary[curClustError] = centroid	
