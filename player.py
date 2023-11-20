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
		if field > gameboard.size ** 2:
			raise ValueError(f"Your chosen field must be smaller than {gameboard.size ** 2}, {field} was entered")

		row = (field - 1) // gameboard.size
		col = (field - 1) % gameboard.size
		if isinstance(gameboard.board[row][col], int):
			gameboard.board[row][col] = self.symbol
		else:
			raise ValueError("Field already occupied... Try another field.")
		
		return (row, col)

	def automatic_move(self, gameboard):
		field = random.randint(1, gameboard.size ** 2)
		return self.move(field, gameboard)