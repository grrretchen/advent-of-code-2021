import numpy as np
from collections import Counter
from pprint import pprint as pp
import re


class HeightMap:
	def __init__(self,dataset):
		self.dataset = dataset
		self.np = np.array(dataset)

		self.growSet()
		self.depth = np.zeros(self.np.shape, dtype=int)

		print(self.np)
		print(self.depth)
		self.compare()

	def compare(self):

		home = self.np.copy()

		left = np.roll(self.np.copy(),1,axis=1)
		print(left)

		alpha = home-left
		alpha = np.where((alpha)<0, -1, (alpha))
		alpha = np.where((alpha)>0, 1, (alpha))
		self.depth += alpha
		print(self.depth)
		# print(result)
		# print(np.where((self.np - left)<0,-1))


		# move everything left
		# self.depth = self.np - mask
		# print(self.depth)

	def growSet(self):
		# expand the width by duplicating the first and last columns
		self.np = np.append(self.np[[0],:], self.np, 0)
		self.np = np.append(self.np, self.np[[-1],:], 0)

		# expand the height by duplicating the first and last rows
		self.np = np.append(self.np[:,[0]], self.np, 1)
		self.np = np.append(self.np, self.np[:,[-1]], 1)
		

# --------------------------------------------------------------------------	
# pull the dataset from a file 
def parse(dataset):
	displays = []
	for row in dataset:
		displays.append(Display(inputs = row[0], outputs=row[1]))
	return(displays)


# --------------------------------------------------------------------------	
# pull the dataset from a file 
def fetch(fpath):
	dataset = []
	
	with open(fpath, "r") as infile:
		for line in infile:
			dataset.append([int(i) for i in line.strip()])
				
	print(dataset)
	return dataset


# --------------------------------------------------------------------------	
# solve the problems.
def solve(dataset):
	hm = HeightMap(dataset)

	result1 = None
	result2 = None

	return (result1, result2)	


# --------------------------------------------------------------------------
# do the main 
def main():
	fpath = "./day09-sample.txt" # this is the sample dataset.
	# fpath = "./day09-data.txt"

	dataset = fetch(fpath)

	# displays = parse(raw)
	
	r1,r2 = solve(dataset)

	print(f"Part 1:\t{r1}\r\nPart 2:\t{r2}")	


# ==========================================================================
if __name__ == "__main__" :
	result = main()
