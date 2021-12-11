import numpy as np
from collections import Counter
from pprint import pprint as pp
import re


# ===========================================================================
# track each basin area individually, and implement a floodfill for any values under 9.
class Basin:
	def __init__(self,origin,dataset):
		self.origin = origin 								# received as an (x,y) pair 
		self.dataset = dataset								# received as a 2d numpy array

		self.flood(self.origin[0],self.origin[1])			# floodfill from the origin
		self.size = np.sum(np.where(self.dataset==1,1,0))	# store the number of cells filled


	# floodfill routine which flips zeros to ones, and stops at a 9.
	def flood(self,x,y):
		# skip the cell if already checked, or if a boundary.
		if self.dataset[x, y] in [1,9]:
			return
		if self.dataset[x, y] == 0:
			self.dataset[x, y] = 1

		# scan w/a/s/d
		self.flood(x-1, y)
		self.flood(x+1, y)
		self.flood(x, y-1)
		self.flood(x, y+1) 


# ===========================================================================
# manage the entire map within a single class.
class HeightMap:
	def __init__(self,dataset):
		# receive a 2d array of lists, convert to a numpy array, and add a border of 9s.
		self.np = np.pad(np.array(dataset), 1, mode="constant", constant_values=9)

		# init a depthmap with zeros
		self.np_depth = np.zeros(self.np.shape, dtype=int)
		self.np_basin = np.zeros(self.np.shape, dtype=int)
		self.find_floor()


	# find the lowest point among neighbors
	def find_floor(self):

		# set up temporary arrays which shift up/down/left/right
		w = np.roll(self.np.copy(),-1,axis=0)
		a = np.roll(self.np.copy(),-1,axis=1)
		s = np.roll(self.np.copy(),1,axis=0)
		d = np.roll(self.np.copy(),1,axis=1)
		
		# mask the current cell against the shifted cells, and sink the current cell if we're lower.
		for e in [w,a,s,d]:
			r = self.np.copy() - e
			r = np.where((r)<0, -1, (r))
			r = np.where((r)>0, 1, (r))
			self.np_depth += r


	# part1 result is the sum of [1 + original value] for each of the lowest points of the map. 
	def part1(self):		
		r1 = np.where(self.np_depth==-4, self.np, 0)	# original height
		r2 = np.where(self.np_depth==-4, 1, 0)			# plus 1
		r3 = np.sum([r1+r2])							# equals height plus 1
		return(r3)
		

	# part 2 is the sum of the three largest basin areas.
	def part2(self):
		# get a list of coords of the lowest points.
		basin_pits = np.dstack(np.where(self.np_depth==-4))[0]
		# make a map where the walls are 9s, and the floors are zeros
		basin_walls = np.where(self.np==9, self.np, 0)

		# create an array of basins, based on each basin pit.
		self.basins = [Basin(bp, basin_walls.copy()) for bp in basin_pits]

		# collect the sizes of each basin, sort from low to high
		sums = [b.size for b in self.basins]
		sums.sort()

		# multiply the three largest basins.
		top3 = sums[-3] * sums[-2] * sums[-1]
		return(top3)


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
	result2 = hm.part2()

	return (result1, result2)	


# --------------------------------------------------------------------------
# do the main 
def main():
	# fpath = "./day09-sample.txt" # this is the sample dataset.
	fpath = "./day09-data.txt"
	dataset = fetch(fpath)
	
	r1,r2 = solve(dataset)

	print(f"Part 1:\t{r1}\r\nPart 2:\t{r2}")	


# ==========================================================================
if __name__ == "__main__" :
	result = main()
