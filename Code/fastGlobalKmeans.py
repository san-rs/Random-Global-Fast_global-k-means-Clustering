import numpy as np
import math

import randomKmeans

class fastGlobal:
	
	# constructor
	def __init__(self, numBuck):
		self.globalDictionary = {}
		self.bucketList = {}
		self.numBuckets = numBuck
		self.kd = 0

	# function to check if a number is power of 2
	def is_power2(self, num):
		return ((num & (num - 1)) == 0) and num != 0
	
	# function to build a k-dimensional tree
	def buildTree(self, samples, depth = 0):
		numSamples = len(samples)
		requiredDepth = math.ceil(math.log(self.numBuckets,2))
		bucketIndex = str(depth + 0.1)
		
		if numSamples <= 0 or depth > requiredDepth:
			return None   

		# change axis in each iteration
		axis = depth % self.kd
		sortedPoints = sorted(samples, key=lambda point: point[axis])
		count = 1
		
		while (1):
			if bucketIndex in self.bucketList:	
				bucketIndex = str(int(depth)) + "." + str(count)
				count = count + 1
			else:
				break;
		
		self.bucketList[bucketIndex] = sortedPoints

		# recursive call to generate right and left child
		return {
		'bucket':sortedPoints,
			'point': sortedPoints[numSamples / 2],
			'left': self.buildTree(sortedPoints[:numSamples / 2], depth + 1),
			'right': self.buildTree(sortedPoints[numSamples/2 + 1:], depth + 1)
		}

	# fast global k-means with kd-tree initialization
	def fastGlobal(self, samples, k, tolerance):
		self.kd = len(samples[0])
		bucketKey = []
		tempClusterList = []
		tempClusterList.append(np.array(samples[0]));	 
		curClustError, centroid, clusterList = randomKmeans.randomKmeans(samples, 1, tolerance, tempClusterList)
		centroidList = []
		centroidList.append(np.array(centroid[0]))

		# generate the kd Tree for the given set of samples
		tree = self.buildTree(samples)	
		
		# code to choose the tree branches using index key generated. Not using tree traversel to reduce computational cost
		if self.is_power2(self.numBuckets):
			count = 1
			curBucketIndex = math.ceil(math.log(self.numBuckets,2))
			while (count <= self.numBuckets):
				bucketIndex = str(int(curBucketIndex)) + "." + str(count)
				count = count + 1
				bucketKey.append(bucketIndex)
		else:
			count = 1
			curBucketIndex = math.floor(math.log(self.numBuckets,2))
			numBucketIndex = pow(2,curBucketIndex)

			while (count <= numBucketIndex):
				bucketIndex = str(int(curBucketIndex)) + "." + str(count)
				count = count + 1
				bucketKey.append(bucketIndex)

			indexToRemove = self.numBuckets - numBucketIndex
			
			for count in range(0,int(indexToRemove + 1)):
				bucketKey.pop(0)
			
			nextBucketIndex = curBucketIndex + 1
			count = 0
			indexCount = 1
			
			while (count < int(indexToRemove*2)):
				newBucketIndex = str(int(nextBucketIndex)) + "." + str(indexCount)	
				indexCount = indexCount + 1
				if newBucketIndex not in self.bucketList:
					raise notInList('newBucketIndex not in bucketList')
				bucketKey.append(newBucketIndex)
				count = count + 1

		# from the buckets, find the possible insertion location by finding the center of the bucket
		newCentroidList = []
		for index in bucketKey:
			zipped = zip(*self.bucketList[index])
			num = len(self.bucketList[index])
			newCentroidList.append([math.fsum(dList)/num for dList in zipped])

		# run k-means for the potential insertion points calculated from above
		for kVal in range(2, k+1):
			b = []
			for xn in range(0,len(newCentroidList)):
				bSum = 0
				for clusterIndex in range(0,len(clusterList)):
					for xj in range(len(clusterList[clusterIndex])):
						dj = abs(randomKmeans.sqEucliDist(clusterList[clusterIndex][xj], centroidList[clusterIndex], len(centroidList[clusterIndex])))
						dn = abs(randomKmeans.sqEucliDist(clusterList[clusterIndex][xj], newCentroidList[xn], len(centroidList[clusterIndex])))
						bSum = bSum + max(dj - dn, 0)
				b.append(bSum)
			bIndex = b.index(max(b))
			tempClusterList = []
			tempClusterList.extend(centroidList)
			tempClusterList.append(np.array(newCentroidList[bIndex]));
			curClustError, centroid, clusterList = randomKmeans.randomKmeans(samples, kVal, tolerance, tempClusterList)	
			centroidList = []
			for index in range(0, kVal):
				centroidList.append(np.array(centroid[index]))

		return round(curClustError, 4), centroidList
		