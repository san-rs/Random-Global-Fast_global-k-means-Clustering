import numpy as np
import math

import randomKmeans

def globalKmeans(samples, k, tolerance):
	newCentroid = []
	tmpClusterList = []
	tmpClusterList.append(np.array(samples[0]));	 
	cur_clustError, centroid, clusterList = randomKmeans.randomKmeans(samples, 1, tolerance, tmpClusterList)
	centroidList = []
	centroidList.append(np.array(centroid[0]))
		
	# run k means for each cluster
	for i in range(2, k+1):
		# run k-means for all samples
		for j in range(0,len(samples)):
			tmpClusterList = []
			tmpClusterList.extend(centroidList)
			tmpClusterList.append(np.array(samples[j]));
			cur_clustError, centroid,clusterList = randomKmeans.randomKmeans(samples, i, tolerance, tmpClusterList)
				
			if(j == 0):
				prev_clustError = cur_clustError

			if(cur_clustError <= prev_clustError):
				prev_clustError = cur_clustError
				newCentroid = centroid
		# compile new centroid list	
		centroidList = []
		for index in range(0, i):
			centroidList.append(np.array(newCentroid[index]))
			
	return round(prev_clustError, 4), centroidList