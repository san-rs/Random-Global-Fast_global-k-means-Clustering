# Random, Global, Fast global k-means
	
Compiler/OS requirements:
	- Tested on Windows, Linux and Unix environments
	- No specific compiler/OS requirements

Packages to be installed before running code files:
	- Instructions to install external libraries are given below

	pip/anaconda - use pip or anaconda for installing the required python libraries given below
	
	1. numpy - pip install numpy
	2. pandas - pip install pandas
	3. matplotlib - pip install matplotlib
	4. scipy - pip install scipy
	5. sklearn - pip install sklearn

Execution Instructions:
	- To run all the algorithms (k-means, global k-means and fast global k-means) and for visualized graph of results, give the below command in terminal
			
			python plotFinalData.py

	- The results and progress would be shown on the terminal/screen and the graph would be displayed after execution
	- Explanation of input parameters
			* The required algorithms are called by passing the right parameters.
					randomKmeans(samples, numK, tolerance, centroidList)
					globalKmeans(samples, numK, tolerance)
					fastGlobal(samples, numK, tolerance)
			 where,
					samples are the input samples loaded by the functions, loadMOG and loadMNIST as defined in loadData.py
					numk is the number of clusters
					tolerance is 0.001
					centroidList is the list of initial random cluster centroids upon which the randomKmeans algorithm has to run

Generate input file:
	- Mixture of Gaussians input file can be generated by running the below command in terminal.
			python genMixOfGau.py
	- Mixture of Gaussians data size to be generated can be modified in the file 'genMixOfGau.py'.
	- MNIST data of size 500 and 1000 are submitted along with the submission, inside 'Data' folder. Larger size MNIST data can be downloaded from the link provided in 'cse569_project.pdf' under Project 1 description. Full sized data is not included as its size is large and submission exceeds 50 mb.

Notes:
	- Check the Output Screenshots folder for all the screenshots for all the 3 algorithms.
	- Global k-means is computational intensive and hence is not advisable to run on large set of data. Execution of 500 data with 10 features each and 10 clusters takes around 3 hours. Execution of k-means clustering on the entire MNIST train set of 60000 data takes around 10 minutes. Execution of fast global for 500 data with 10 features each and 10 clusters takes 15 seconds
	- Because of this, as advised by TA, the executions are run on a subset data of size 500 and 1000, the results of which can be seen in the Output Screenshots folder.
