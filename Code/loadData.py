import numpy
import math
import pandas as pd
from sklearn.decomposition import PCA

def loadMOG(infile):
	data=open(infile);
	lines=data.readlines()
	samples=[];
	for line in lines:
		line=line.strip()
		line=line.split('\t')
		line=filter(None,line)
		line=map(float,line)
		value=(line) 
		samples.append(line)
	return samples

def loadMNIST():
	temp = pd.read_csv('mnist_500.csv', header = None, usecols = range(1,785))
	#print temp.shape
	pca = PCA(n_components = 10)
	samples = pca.fit_transform(temp)
	#print samples.shape
	return samples