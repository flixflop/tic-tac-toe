class GameBoard:
	
	def __init__(self):
		self.board = []
		self._create_board()

	def _create_board(self):
		for i in range(3):
			self.board.append([None] * 3)

	def _has_winner(self):

	
		### Another way to check for a winner:
		### For all winning cells --> concat a string, if it contains three identical characters someone won.
		board_strings = []
		for i in range(3):
			r = ""
			c = ""
			for j in range(3):
				if self.board[i][j]:
					r += self.board[i][j]
					board_strings.append(r)

				if self.board[j][i]:
					c += self.board[j][i]
					board_strings.append(c)

		return board_strings

			



	def _render_board(self):
		"""
		 _ _ _ _ _ _ _ _ _
		|     |     |     |
		|_ _ _|_ _ _|_ _ _|
 		|     |     |     |
		|_ _ _|_ _ _|_ _ _|
		|     |     |     |
		|_ _ _|_ _ _|_ _ _|       

		"""