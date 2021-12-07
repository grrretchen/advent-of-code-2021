from collections import Counter
import numpy as np
from datetime import datetime as dt
# =============================================================================
class School:
	def __init__(self, fish):
		self.fish = Counter(fish)

	def update(self):
		# age the current fish
		self.fish = {k-1:v for k,v in self.fish.items()}
		
		# span the new fish by counting the "-1" fish, and creating new eights.
		self.fish[8] = self.fish.pop(-1,0)

		# recycle the dead fish by counting the babies (the 8s) and adding them to the 6s
		self.fish[6] = self.fish[8] if not 6 in self.fish else self.fish[6] + self.fish[8]


# -----------------------------------------------------------------------------	
# pull the dataset from a file 
def fetch(fpath):
	dataset = []
	
	with open(fpath, "r") as infile:
		dataset = [int(i) for i in infile.read().split(",")]
				
	return dataset


# -----------------------------------------------------------------------------
# Age the school by x number of days, and return the sum of fish..
def age(dataset, days):
	school = School(dataset)
	print(dataset)
	for i in range(days):
		school.update()
		print(f"\tCycle: \t{i+1}\tCount: \t{sum(school.fish.values())}")
	return(sum(school.fish.values()))
	

def align(dataset):
	# make a numpy array. (duh)
	np_ds = np.array(dataset)
	c_ds = Counter(np_ds)
	# assume that several crabs are already in position, and only use those positions.
	spots = {i:0 for i in np.unique(np_ds)}
	print(spots)

	# iterate over each spot, and determine the offset.
	for spot in spots:
		print(f"\n{spot} -----------------------")
		print(np_ds)
		np_a = np_ds - spot
		print(np_a)
		
#		a = {k-spot:v for k,v in c_ds.items()}
		# b = sum[abs(a)]
		a_neg = np.where(np_a<0)
		a_pos = np.where(np_a>0)
		print(f"{a_neg} < 0 < {a_pos}")
		moves = abs(np.sum(a_neg)+abs(np.sum(a_pos)))
		print(moves)
		# print(spots[spot])

	#print(np_ds)
	exit()

	print(dataset)
	ds = Counter(dataset)
	print(*dataset)
	print(ds)

	
	
# -----------------------------------------------------------------------------
# do the main 
def main():
	fpath = "./day07-sample.txt" # this is the sample dataset.
	#fpath = "./day07-data.txt"
	dataset = fetch(fpath)
	
	align(dataset)
	exit()
	part0 = age(dataset, days=18)
	part1 = age(dataset, days=80)
	part2 = age(dataset, days=256)

	print(f"Part 1:\t{part1}\r\nPart 2:\t{part2}")	
	

# =============================================================================
if __name__ == "__main__" :
	result = main()
