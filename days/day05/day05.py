from pprint import pprint as pp
import numpy as np

class board:
	def __init__(self, pointset):
		self.pointset = pointset
		# two arrays, one for the digits, and one for the matches
		self.lines = np.array(pointset)
		self.max = np.amax(self.lines) + 1
		self.map = np.zeros((self.max, self.max), dtype=int)
		print(self.lines)
		print(self.map)

		self.makemap()
		
		print(self.map)
	
	def makemap(self):
		print("makemap")
		for pair in self.lines:
			#print("line ---------")
			print(pair)
			
			x_rg = [ pair[0,0], pair[1,0] ]
			y_rg = [ pair[0,1], pair[1,1] ]
			x_dir = 1 if x_rg[1] > x_rg[0] else -1
			x_dir = 0 if x_rg[0] == x_rg[1] else x_dir
			y_dir = 1 if y_rg[1] > y_rg[0] else -1
			y_dir = 0 if y_rg[0] == y_rg[1] else y_dir
			x_len = abs(x_rg[0] - x_rg[1])+1
			y_len = abs(y_rg[0] - y_rg[1])+1
			
			for i in range(x_len if x_len > y_len else y_len):
				x = pair[0,0] + ( i * x_dir )
				y = pair[0,1] + ( i * y_dir )
				
				# print(f"{x}, {y}")
				self.map[y,x] += 1
				
				"""
				for y in range(y_rg[0], y_rg)
				self.map[x_rg
			if pair[0,0] == pair[1,0]:
				x = pair[0,0]
				rg = [ pair[0,1], pair[1,1] ]
				rg.sort()
				#print(rg)
				for y in range(rg[0], rg[1] + 1):
					#print(y)
					self.map[x,y] += 1# = self.map[x,y]+1
			if pair[0,1] == pair[1,1]:
				y = pair[0,1]
				#print("same y")
				rg = [ pair[0,0], pair[1,0] ]
				rg.sort()
				#print(rg)
				for x in range(rg[0], rg[1] + 1):
					#print(x)
					self.map[x,y] += 1# = self.map[x,y]+1
					"""
			
		print(np.count_nonzero(self.map>=2))
			
		
		#max_x = np.amax(self.lines)
		#print(max_x)
		
	# we'll use this with every new token.
	def play(self, token):
		print(f"Playing {token}")
		self.token = token
		
		# don't bother if we don't have this number on the board
		if not np.count_nonzero(self.np_board==token): 
			return False
	
		# set the corresponding position for the other matrices
		self.np_match[np.where(self.np_board==token)] = 1
		self.np_score[np.where(self.np_board==token)] = 0
		
		# print(self.np_board)
		# print(self.np_match)
		
		return self.score()
		
	# calculate each row, each column, and the overall score.
	# return the total score if we have bingo, else False.
	def score(self):
		# always keep the total score up-to-date.
		self.total_score = np.sum(self.np_score)
		self.aoc_score = self.total_score * self.token
		
		# make a sum of the number of matches per row, or per column
		self.score_x = np.sum(self.np_match, axis=0)
		if 0 <= np.where(self.score_x==5)[0]:
			self.is_solved = True
			
		self.score_y = np.sum(self.np_match, axis=1)
		if 0 <= np.where(self.score_y==5)[0]:
			self.is_solved = True
		
		# if we have a full row, then return the total board score.
		if self.is_solved:
			return self.total_score
		
		return False	
		
		
# generate a data set from a sample, or from a file. --------------------------
def sample(fpath):
	dataset = []
	
	with open(fpath, "r") as infile:
		for line in infile:
			# some of these lines might be blank, so skip those.
			try:
				dataset.append(line)
			except:
				continue
				
	result = [a.strip() for a in dataset]
	return result

# --------------------------		
# break the dataset into a list of gameplay tokens, and all the gameboards.
def parse(dataset):
	coordinates = []
	
	# create a 3d-nested array like [ [ [x, y], [x, y] ], ... ]
	for row in dataset:
		coords = [[int(x),int(y)] for x,y in [pair.split(",") for pair in row.split(" -> ")]]
		coordinates.append(coords)
	
	return coordinates
			

		
# do the main -----------------------------------------------------------------
def main():
	#fpath = "./day05-sample.txt" # this is the sample dataset.
	fpath = "./day05-data.txt"
	dataset = sample(fpath)
	
	lineset = parse(dataset)
	print(lineset)
	
	myMap = board(lineset)
	
	
	
	
	
# =============================================================================
if __name__ == "__main__" :
	result = main()

