from collections import Counter
from numpy import median
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
	#dataset.sort
	print(sum(dataset))
	print(median(dataset))
	#print(mean(dataset))
	pos = Counter(dataset)
	print(pos)
	print(len(pos))
	print(pos.keys())
	print(pos.items())
	for p in pos.items():
		# sum of total possible moves, minus the moves canceled by this position
		print((sum(dataset)-p[0]*p[1]))#- (p[0]*len(dataset)))
	
	
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
