import numpy as np
import pandas as pd
import math
import random
import datetime
import matplotlib as mpl
mpl.use('TkAgg')
import matplotlib.pyplot as plt

import randomKmeans
import globalKmeans
import fastGlobalKmeans
import loadData

def main():
	print('\nLoading data: {:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now()))
	samples = loadData.loadMOG('MixOfGau.txt')
	print('Loading complete: {:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now()))
	
	numK = [5, 10]
	numBuckets = len(samples)/2
	kmeansClustError = [0]*len(numK)
	globalClustError = [0]*len(numK)
	fastClustError = [0]*len(numK)
	tolerance = 0.001
	centroidList = []	
	fg = fastGlobalKmeans.fastGlobal(numBuckets)
	
	for index in range(len(numK)):
		centroidList = random.sample(samples, numK[index])
		
		print('\nStart of random k-means: {:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now()))
		kmeansClustError[index], kmeansClustList, P = randomKmeans.randomKmeans(samples, numK[index], tolerance, centroidList)
		print('End of random k-means: {:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now()))
		
		print('\nStart of global k-means: {:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now()))
		globalClustError[index], globalClustList = globalKmeans.globalKmeans(samples, numK[index], tolerance)
		print('End of global k-means: {:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now()))

		print('\nStart of fast global k-means: {:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now()))
		fastClustError[index], fastClustList = fg.fastGlobal(samples, numK[index], tolerance)
		print('End of fast global k-means: {:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now()))

		
	print "\n\nRandom k-means: clustering error = " + str(kmeansClustError)
	print "Global k-means: clustering error = " + str(globalClustError)
	print "Fast global k-means: clustering error = " + str(fastClustError)
	
	x = [];
	y1 = [];
	y2 = [];
	y3 = [];

	for i in numK:
		x.append(i)

	for i in kmeansClustError:
		y1.append(i)

	for i in globalClustError:
		y2.append(i)

	for i in fastClustError:
		y3.append(i)

	plt.plot(x, y1, 'r+');
	plt.plot(x, y2, 'bo');
	plt.plot(x, y3, 'g*');	
	plt.axis();
	plt.xlabel('Number Of Clusters k');
	plt.ylabel('Clustering Error');
	text = "+ is random\no is global\n* is fast"
	plt.text(0.02, 0.7, text, fontsize = 14, transform = plt.gcf().transFigure)
	plt.subplots_adjust(left = 0.28)
	plt.show();

if __name__ == "__main__":
	main()