import numpy as np
from collections import Counter
from pprint import pprint as pp
import re

class Display:
	def __init__(self, inputs, outputs):
		self.digits = Counter(self.scrub(inputs + outputs))
		self.outputs = self.scrub(outputs)
		
		self.map = ["zzzzzzz"] * 10
		self.remap = {}
		self.makemap()
		self.map1478 = [self.map[1],self.map[4],self.map[7],self.map[8]]
		
		self.makeOutput()


	def makeOutput(self):
		# sum1 (count 1478 digits)
		self.output1478 = sum([Counter(self.outputs)[m] for m in self.map1478])

		# sum2 (full output)
		self.output = int("".join([str(self.remap[a]) for a in self.outputs]))
		# self.output = int(alpha)


	def scrub(self, input):
		result = []
		for each in input:
			raw = [c for c in each]
			raw.sort()
			result.append( "".join(raw) )
		return result

	def makemap(self):
		# the key digits are 1, 4, and 7.
		for digit in self.digits:
			if len(digit) == 2:
				self.map[1] = digit
			if len(digit) == 4:
				self.map[4] = digit
			if len(digit) == 3:
				self.map[7] = digit
			if len(digit) == 7:
				self.map[8] = digit
		
		while 'zzzzzzz' in self.map:
			for digit in self.digits:
				if digit in self.map:
					continue
				try:	
					if len(digit) == 6:
						if re.findall(".*".join([i for i in self.map[4]]), digit):
							self.map[9] = digit
						elif re.findall(".*".join([i for i in self.map[7]]), digit):
							self.map[0] = digit
						else:
							self.map[6] = digit
					if len(digit) == 5:
						if re.findall(".*".join([i for i in self.map[7]]), digit):
							self.map[3] = digit
						elif re.findall(".*".join([i for i in digit]), self.map[9]):
							self.map[5] = digit
						else:
							self.map[2] = digit
				except:
					continue

		for digit in range(len(self.map)):
			self.remap[self.map[digit]] = digit
		

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
			row = [i.strip().split(" ") for i in line.strip().split("|")]
			dataset.append(row)
				
	return dataset


# --------------------------------------------------------------------------	
# solve the problems.
def solve(displays):
	sums1 = sum([d.output1478 for d in displays])
	sums2 = sum([d.output for d in displays])

	return (sums1, sums2)	


# --------------------------------------------------------------------------
# do the main 
def main():
	fpath = "./day08-sample.txt" # this is the sample dataset.
	# fpath = "./day08-data.txt"

	dataset = fetch(fpath)

	displays = parse(dataset)
	
	part1,part2 = solve(displays)

	print(f"Part 1:\t{part1}\r\nPart 2:\t{part2}")	


# ==========================================================================
if __name__ == "__main__" :
	result = main()
