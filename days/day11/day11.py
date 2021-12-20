import numpy as np
from time import sleep

class Pod:
	def __init__(self, board):
		self.board = np.array(board)
		self.last = self.board.copy()
		self.this = self.board.copy()
		print(self.board)
		
		self.age()
		
	def step(self):
		# set alpha to the board
		alpha = self.board.copy()
		
		# First, the energy level of each octopus increases by 1.
		beta = np.ones_like(last, dtype=int) + self.this
		
		# Then, any octopus with an energy level greater than 9 flashes. 
		# This increases the energy level of all adjacent octopuses by 1, 
		# including octopuses that are diagonally adjacent.
		while not np.all(beta==alpha):
			print("while")
			# set alpha to the previous result.
			alpha = beta.copy()

			# recursively set beta to the result of beta
			beta=self.flash(beta)

			# exit while if alpha==beta
			if (beta == alpha):
				print("exit loop")
				break

		# show the result of this step.
		print("step result")
		print(beta)
		self.last = beta


	def flash(self,matrix):
		# pad the dataset by 1 cell.
		alpha = np.pad(matrix,(1,1),"constant",constant_values=0)
		
		# This increases the energy level of all adjacent octopuses by 1, 
		# including octopuses that are diagonally adjacent.
		# get all of the coordinates which are gt nines.
		nines=np.argwhere(alpha>9)
		
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
			# beta = np.where(beta>=9, 9, beta)
			print(beta)
			sleep(0.1)
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
