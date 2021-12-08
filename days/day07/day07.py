# --------------------------------------------------------------------------	
# pull the dataset from a file 
def fetch(fpath):
	dataset = []
	
	with open(fpath, "r") as infile:
		dataset = [int(i) for i in infile.read().split(",")]
				
	return dataset


# --------------------------------------------------------------------------
# find the position which require the least number of moves.
def align(dataset):
	dataset.sort
	
	c1 = float('inf')
	c2 = float('inf')
	for i in range(min(dataset),max(dataset)):
		a1= [abs(c-i) for c in dataset]
		c1 = min(c1,sum(a1))
		
		a2 = [( (abs(c-i)*(abs(c-i)+1))//2) for c in dataset]
		c2 = min(c2,sum(a2))

	return (c1,c2)
	
	
# --------------------------------------------------------------------------
# do the main 
def main():
	#fpath = "./day07-sample.txt" # this is the sample dataset.
	fpath = "./day07-data.txt"
	dataset = fetch(fpath)
	
	part1,part2 = align(dataset)

	print(f"Part 1:\t{part1}\r\nPart 2:\t{part2}")	


# ==========================================================================
if __name__ == "__main__" :
	result = main()
