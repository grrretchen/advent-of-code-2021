import numpy as np
import logging
import sys
from time import sleep

LogFormat = "%(levelname)s \t%(asctime)s \t%(message)s"
LogLevel = logging.DEBUG

logging.basicConfig(
	stream=sys.stdout,
	format=LogFormat,
	level=LogLevel
	)
logger = logging.getLogger()

# =============================================================================
class Pod:
	def __init__(self, board):
		self.board = np.array(board)
		self.last = self.board.copy()
		self.this = self.board.copy()	
		self.flashes = 0 # part 1 - count the total of all flashes.
		self.safe = [] # part 2 - identify the first frame where all octopi flash at once.
		self.loop(count=300)
		

	def loop(self,count):
		for i in range(count):
			logger.info(f"LOOP {i+1} ===================================")
			self.step()
			print(f"\nAfter step {i+1}:")
			print(self.this)
			print(self.flashes)
			if np.array_equal(np.zeros_like(self.this, dtype=int), np.where(self.this==0,0,1)):
				self.safe.append(i+1)
				break

			self.last = self.this

	# -------------------------------------------------------------------------
	def step(self):
		# logger.debug("STEP ------------------------")
		
		# First, the energy level of each octopus increases by 1.
		self.this = self.last + np.ones_like(self.last, dtype=int)

		# quickly return if none of the octopus are mature.
		if not np.any(self.this > 9):
			self.last = self.this
			return

		# Any octopus with an energy level greater than 9 flashes. 
		# This increases the energy level of all adjacent octopuses
		self.glowup()

		# Any octopus that flashed during this step has its energy
		# level set to 0, as it used all of its energy to flash.
		self.this = np.where(self.this>9,0,self.this)

		# count the flashes within this frame, and add to the total.
		flashes = np.sum(np.where(self.this==0,1,0))
		self.flashes += flashes
		

	# -------------------------------------------------------------------------
	def glowup(self):
		# since an octopus can trigger adjacent octopus within each step, 
		# we'll call these "slaves", 
		# and set up a buffer to identify the new slaves within each sub-frame.		
		slaves_0 = np.zeros_like(self.this)
		slaves_1 = np.where(self.this>9,1,0)
		slaves_new = slaves_1 - slaves_0

		while np.any(slaves_new>0):
			# update the frame for only the new slaves.
			self.roll(slaves_new)

			# set up the state for the next round
			slaves_0 = slaves_1
			slaves_1 = np.where(self.this>9,1,0)
			slaves_new = slaves_1 - slaves_0
					

	# -------------------------------------------------------------------------
	def roll(self,slaves):
		# roll a frame around each octopus that flashes, to increase adjacent octopus by 1.

		# pad the entire dataset by 1 cell, to create a margin.
		alpha = np.pad(self.this,(1,1),"constant",constant_values=0)
				
		# create a 3x3 mask, and zero-pad to match size of dataset
		mask = np.pad(
			np.ones((3,3), dtype=int), 
			(0,alpha.shape[0]-3),
			"constant", 
			constant_values = 0)
		mask[1,1] = 0
		
		# find anything greater than 9.
		tens=np.argwhere(slaves>0)

		# create an overlay which measures the increase per octopus
		overlay = np.zeros_like(alpha)

		# roll the 3x3 overlay around to each mature octopus.
		for ten in tens:
			r = mask.copy()
			r = np.roll(r,ten[0],axis=0)
			r = np.roll(r,ten[1],axis=1)
			
			overlay = r + overlay

		# add the overlay to the original dataset.
		beta = alpha + overlay
		self.this = beta[1:-1,1:-1]
		
		
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
	result1 = board.flashes
	result2 = board.safe

	return (result1, result2)	


# --------------------------------------------------------------------------
# do the main 
def main():
	# fpath = "./day11-sample.txt" # this is the sample dataset.
	fpath = "./day11-data.txt"
	dataset = fetch(fpath)
	
	r1,r2 = solve(dataset)
	print(f"Part 1:\t{r1}\r\nPart 2:\t{r2}")	


# ==========================================================================
if __name__ == "__main__" :
	result = main()
