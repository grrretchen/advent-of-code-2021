from pprint import pprint as pp
import numpy as np

class board:
	def __init__(self, board):
		# two arrays, one for the digits, and one for the matches
		self.board = board if board else [ [0] * 5 ] * 5
		self.match = [ [0] * 5 ] * 5
		self.is_solved = 0
		
		# set up three arrays to track the board, the tokens, and the blanks.
		self.np_board = np.array(self.board)
		self.np_match = np.array(self.match)
		self.np_score = np.array(self.board)
		
		# store the status of the x array, the y array, and the total.
		self.total_score = 0
		self.aoc_score = 0
		self.score_x = [0] * 5
		self.score_y = [0] * 5
		
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
	tokens = []
	boards = []
	
	b = []
	match = []
	
	for row in dataset:
		if "," in row:
			tokens = [int(i) for i in row.split(",")]
		elif len(row) == 0:
			b = []
		else:
			b.append([int(i) for i in row.split()])
		if len(b) == 5:
			nb = board(b)
			boards.append(nb)
			
			
			
	result = {
	"tokens" : tokens,
	"boards" : boards
	}
	
	pp(result)
	return result
	
# --------------------------
def play(boards, tokens):
	board_scores = []
	for token in tokens:
		for board in boards:
			if board.is_solved:
				continue
			print("=====================")
			result = board.play(token)
			if result:
				board_scores.append(board.aoc_score)
				board.is_solved = len(board_scores)
			if len(board_scores) == len(boards):
				print("all boards completed")
				
	print("=====================")
	print(f"First win: {board_scores[0]}")
	print(f"Last win: {board_scores[-1]}")
		
# do the main -----------------------------------------------------------------
def main():
	#fpath = "./day04-sample.txt" # this is the sample dataset.
	fpath = "./day04-data.txt"
	dataset = sample(fpath)
	
	gameset = parse(dataset)
	
	play(gameset["boards"], gameset["tokens"])
	
# =============================================================================
if __name__ == "__main__" :
	result = main()

