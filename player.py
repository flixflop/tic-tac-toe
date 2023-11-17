class Player:

	def __init__(self, symbol):
		self.symbol = symbol

	def play(self, field, board):
		"""
		field: int between 0 and 9
		board: GameBoard
		"""
		# we need to map 0 - 9 to matrix entry i.e. 0 -> 0, 0
		if field > 8:
			raise ValueError(f"Field must be smaller than 9, {field} was entered")

		row = field // 3
		col = field % 3
		board.board[row][col] = self.symbol
