import numpy as np

def main():
	d1 = []
	d2 = []
	d3 = []

	d1.append(np.random.normal(35, 200, 500))
	d2.append(np.random.normal(10, 50, 500))
	d3.append(np.random.normal(55, 125, 500))

	d1 = d1[0]
	d2 = d2[0]
	d3 = d3[0]

	d11 = []
	d22 = []
	d33 = []
	
	for i in d1:
		d11.append(float(i))

	for i in d2:
		d22.append(float(i))

	for i in d3:
		d33.append(float(i))

	f = open("MixOfGau.txt","w+")

	for i in range(0,500):
		f.write(str(round(d11[i], 2)))
		f.write('\t' + str(round(d22[i], 2)))
		f.write('\t' + str(round(d33[i], 2)))
		f.write('\n')
	
	f.close()

if __name__ == "__main__":
	main()