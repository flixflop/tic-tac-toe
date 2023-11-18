class TicTacToe:
	
	def __init__(self, gameboard, player_1=None, player_2=None):
		self.p1 = player_1
		self.p2 = player_2
		self._gb = gameboard

	def play(self):
		header = """
 _____ _        _____            _____          
|_   _(_) ___  |_   _|_ _  ___  |_   _|__   ___ 
  | | | |/ __|   | |/ _` |/ __|   | |/ _ \ / _ \\
  | | | | (__    | | (_| | (__    | | (_) |  __/
  |_| |_|\___|   |_|\__,_|\___|   |_|\___/ \___|
  """
		greeting = """
		Welcome to Tic Tac Toe! The rules are simple, first player to have three in a row
		wins. The fields are labled 0 - 8, you can choose your field by simply inputting 
		the value of the field.
		"""
		print(header)
		print(greeting)
		winner = False
		while not winner:
			self._gb._render_board()
			field = int(input("Player 1 - Choose your field\n>>> "))
			row, col = self.p1.move(field, self._gb)
			self._gb._render_board()
			winner = self._winning_move(row, col, self.p1.symbol)
			if winner:
				print("Player 1 won")
				break
			row, col = self.p2.automatic_move(self._gb)
			self._gb._render_board()
			winner = self._winning_move(row, col, self.p2.symbol)
			if winner:
				print("Player 2 won")
				break

		

	def _winning_move(self, row, col, symbol):
		# could also be renamed "winning move"
		if all(symbol == self._gb.board[row][j] for j in range(3)):
			return True
		
		if all(symbol == self._gb.board[i][col] for i in range(3)):
			return True
		
		if all(symbol == self._gb.board[i][i] for i in range(3)):
			return True
		
		if all(symbol == self._gb.board[i][2 - i] for i in range(3)):
			return True
		
		return False
		
