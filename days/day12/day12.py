import numpy as np
import logging
import sys
from time import sleep


# =============================================================================
		
		
# --------------------------------------------------------------------------	
# pull the dataset from a file 
def fetch(fpath):
	dataset = []
	
	with open(fpath, "r") as infile:
		for line in infile:
			dataset.append(line.split("-"))
				
	return dataset


# --------------------------------------------------------------------------	
# solve the problems.
def solve(dataset):

	result1 = None
	result2 = None

	# return (result1, result2)	
	return 


# --------------------------------------------------------------------------
# do the main 
def main():
	# fpath = "./day12-sample.txt" # this is the sample dataset.
	fpath = "./day12-sample.txt"
	dataset = fetch(fpath)
	
	r1,r2 = solve(dataset)
	print(f"Part 1:\t{r1}\r\nPart 2:\t{r2}")	


# ==========================================================================
if __name__ == "__main__" :
	result = main()
