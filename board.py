class GameBoard:
	
	def __init__(self):
		self.board = []
		self._create_board()

	def _create_board(self):
		self.board = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
			
	def _render_board(self):
		for row in self.board:
			print(row)