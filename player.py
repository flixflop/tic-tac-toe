import random

class Player:

	def __init__(self, symbol):
		self.symbol = symbol

	def move(self, field, gameboard):
		"""
		field: int between 0 and 9
		board: GameBoard
		"""
		# we need to map 0 - 9 to matrix entry i.e. 0 -> 0, 0
		if field > 8:
			raise ValueError(f"Field must be smaller than 9, {field} was entered")

		row = field // 3
		col = field % 3
		if gameboard.board[row][col] != self.symbol:
			gameboard.board[row][col] = self.symbol
		else:
			raise Exception("Field already occupied... Try another field.")
		
		return (row, col)

	def automatic_move(self, board):
		field = random.randint(0, 8)
		return self.move(field, board)