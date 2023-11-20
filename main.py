from board import GameBoard
from player import Player
from tictactoe import TicTacToe

def main():

	# gb = GameBoard(size=5)
	# print(gb.board)

	p1 = Player('x')
	p2 = Player('o')
	b = GameBoard(size=4)
	ttt = TicTacToe(b, p1, p2)

	ttt.play()

if __name__ == "__main__":

	main()