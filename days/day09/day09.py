import numpy as np
from collections import Counter
from pprint import pprint as pp
import re


class HeightMap:
	def __init__(self,dataset):
		self.dataset = dataset
		self.np = np.array(dataset)

		self._expand()
		self.depth = np.zeros(self.np.shape, dtype=int)
		self.flood()
		self.part1()
		self.part2()
		
	def part1(self):
		r1 = np.where(self.depth==-4, self.np, 0)
		r2 = np.where(self.depth==-4, 1, 0)
		r3 = np.sum([r1+r2])
		return(r3)
		
		
	def part2(self):
		print(self.depth)
		print(np.where(self.depth==-4))
		print(np.where(self.depth>0, 8, 1))
		
	def flood(self):

		w = np.roll(self.np.copy(),-1,axis=0)
		a = np.roll(self.np.copy(),-1,axis=1)
		s = np.roll(self.np.copy(),1,axis=0)
		d = np.roll(self.np.copy(),1,axis=1)
		
		for e in [w,a,s,d]:
			r = self.np.copy() - e
			r = np.where((r)<0, -1, (r))
			r = np.where((r)>0, 1, (r))
			self.depth += r
		

	def _expand(self):
		# expand the width by duplicating the first and last columns
		self.np = np.append(self.np[[0],:]+1, self.np, 0)
		self.np = np.append(self.np, self.np[[-1],:]+1, 0)

		# expand the height by duplicating the first and last rows
		self.np = np.append(self.np[:,[0]]+1, self.np, 1)
		self.np = np.append(self.np, self.np[:,[-1]]+1, 1)
		
		
	def _shrink(self):
		for ar in [self.np, self.depth]:
			ar = np.delete(ar, -1, axis=0)
			ar = np.delete(ar, -1, axis=1)
			ar = np.delete(ar, 0, axis=0)
			ar = np.delete(ar, 0, axis=1)
			print(ar)
		
		print(self.np)
		print(self.depth)
		

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
				
	return dataset


# --------------------------------------------------------------------------	
# solve the problems.
def solve(dataset):
	hm = HeightMap(dataset)

	result1 = hm.part1()
	result2 = None

	return (result1, result2)	


# --------------------------------------------------------------------------
# do the main 
def main():
	fpath = "./day09-sample.txt" # this is the sample dataset.
	#fpath = "./day09-data.txt"

	dataset = fetch(fpath)

	# displays = parse(raw)
	
	r1,r2 = solve(dataset)

	print(f"Part 1:\t{r1}\r\nPart 2:\t{r2}")	


# ==========================================================================
if __name__ == "__main__" :
	result = main()
