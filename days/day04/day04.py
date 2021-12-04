from pprint import pprint as pp
import numpy as np

class board:
	def __init__(self, board):
		# two arrays, one for the digits, and one for the matches
		self.board = board if board else [ [0] * 5 ] * 5
		self.match = [ [0] * 5 ] * 5
		
		self.np_board = np.array(self.board)
		
		# score the x array, the y array, and the total.
		self.total_score = 0
		self.score_x = [0] * 5
		self.score_y = [0] * 5
		
		# keep track of all of the digits on the board
		self.digits = [i for i in np.unique([x for y in self.board for x in y])]
		
	# we'll use this with every new token.
	def play(self, token):
		print(f"Playing {token}")
		
		
		pp(self.board)
		pp(self.match)
		
		npcount = np.count_nonzero(self.np_board==token, axis=1)
		print(self.np_board)
		print(npcount)
		print(f"npcount = {npcount}")
		exit()
		
		if not token in self.digits:
			return False
			
		for row in range(len(self.board)):
			for col in range(len(self.board[row])):
				if not token == self.board[row][col]:
					continue
				self.match[row][col] = token
				pp(self.match)
			pp(self.match[row])
			
		return self.score()
		
	# calculate each row, each column, and the overall score.
	# return the total score if we have bingo, else False.
	def score(self):
		pp(self.match)
		return
		b = np.array(self.match)
		print(b)
		print(b.sum(axis=0))
		return False
		#for x in range(5):
		#       self.score_y[x] = sum(i for i in self.board[x][y])
		
		
		
		
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
	
def play(boards, tokens):
	for token in tokens:
		print(token)
		for board in boards:
			print("=====================")
			board.play(token)
		exit()
		
		
		
# do the main -----------------------------------------------------------------
def main():
	fpath = "./day04-sample.txt" # this is the sample dataset.
	#fpath = "./day04-data.txt"
	dataset = sample(fpath)
	
	gameset = parse(dataset)
	
	play(gameset["boards"], gameset["tokens"])
	
	
	
# =============================================================================
if __name__ == "__main__" :
	result = main()

