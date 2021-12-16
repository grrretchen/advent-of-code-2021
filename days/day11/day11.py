import numpy as np
from time import sleep

class Pod:
	def __init__(self, board):
		self.board = np.array(board)
		self.last = self.board.copy()
		self.next = self.board.copy()
		print(self.board)
		
		self.age()
		
	def age(self):
		last = self.board.copy()
		
		# increase all values by one
		next = np.ones_like(last, dtype=int) + self.next
		
		while not np.all(next==last):
			print("-----------")
			diff = next==last
			print(diff)
			last=next.copy()
			next=self.blink(next)
			#next = np.where(next>=9,9,next)
			print("blink")
			
		print("exit loop")
		self.last = next
		print(self.last)
		#self.pnext = 
		
		
		print(self.next[2:4,2:4])
		
	def blink(self,matrix):
		# pad the dataset by 1 cell.
		alpha = np.pad(matrix,(1,1),"constant",constant_values=0)
		
		# get all of the coordinates which are nines.
		nines=np.argwhere(alpha==9)
		
		#create a 3x3 mask for the nines
		mask = np.pad( 
			np.ones((3,3),dtype=int), (0,alpha.shape[0]-3),
			"constant", constant_values = 0)
		
		beta = alpha.copy()
		for nine in nines:
			r = mask.copy()
			r = np.roll(r,nine[0],axis=0)
			r = np.roll(r,nine[1],axis=1)
			
			beta = r + beta
			beta = np.where(beta>=9, 9, beta)
			print(beta)
			sleep(1)
			#beta = np.roll
		
		return(beta[1:-1,1:-1])
		
		
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
	board = Pod(dataset)
	result1 = None
	result2 = None

	return (result1, result2)	


# --------------------------------------------------------------------------
# do the main 
def main():
	fpath = "./day11-sample.txt" # this is the sample dataset.
	#fpath = "./day11-data.txt"
	dataset = fetch(fpath)
	
	r1,r2 = solve(dataset)
	print(f"Part 1:\t{r1}\r\nPart 2:\t{r2}")	


# ==========================================================================
if __name__ == "__main__" :
	result = main()
