import numpy as np
from time import sleep

class Pod:
	def __init__(self, board):
		self.board = np.array(board)
		self.last = self.board.copy()
		self.this = self.board.copy()	

		self.loop(count=2)
		

	def loop(self,count):
		print("Before any steps:")
		print(self.last)
		for i in range(count):
			print("----------------------------")
			self.step()
			print(f"\nAfter step {i+1}:")
			print(self.last)


	def step(self):
		# psuedo-code:
		# - increment all by one.
		# - set blinked to all zeros
		# - loop:
		# -- find the new tens that aren't blinked
		# -- blink the new tens
		# -- store anything 10+ the result of this substep 


		# set alpha to the board
		alpha = self.last.copy()
		
		# First, the energy level of each octopus increases by 1.
		beta = alpha + np.ones_like(alpha, dtype=int)
		
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
			if np.all(beta == alpha):
				print("exit loop")
				break

		# Finally, any octopus that flashed during this step has its energy
		# level set to 0, as it used all of its energy to flash.
		charlie = np.where(beta>9,0,beta)
		
		# show the result of this step.
		print("step result")
		print(beta)
		print(charlie)
		self.last = charlie


	def flash(self,matrix):
		# pad the dataset by 1 cell.
		alpha = np.pad(matrix,(1,1),"constant",constant_values=0)
		
		# This increases the energy level of all adjacent octopuses by 1, 
		# including octopuses that are diagonally adjacent.
		# get all of the coordinates which are gt nines.
		nines=np.argwhere(alpha>9)
		
		#create a 3x3 mask for the nines
		mask = np.pad(
			np.ones((3,3), dtype=int), 
			(0,alpha.shape[0]-3),
			"constant", 
			constant_values = 0)
		mask[1,1] = 0
		
		beta = alpha.copy()
		overlay = np.zeros_like(beta)
		for nine in nines:
			r = mask.copy()
			r = np.roll(r,nine[0],axis=0)
			r = np.roll(r,nine[1],axis=1)
			
			overlay = r + overlay
			# beta = np.where(beta>=9, 9, beta)
			# print(overlay)
			# sleep(0.1)
			#beta = np.roll
		print(beta)
		print(overlay)
		print(beta+overlay)
		sleep(1)
		beta = beta + overlay
		
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
