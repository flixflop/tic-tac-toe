class GameBoard:
	
	def __init__(self, size=3):
		self.size = size
		self.board = []
		self._create_board()

	def _create_board(self):
		for i in range(self.size):
			row = list(range(1 + i * self.size, self.size+1 + i * self.size))
			self.board.append(row)
		#self.board = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
			
	def render_board(self):
		for row in self.board:
			print(row)