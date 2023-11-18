from board import GameBoard
from player import Player
from tictactoe import TicTacToe

def main():

	p1 = Player('x')
	p2 = Player('o')
	b = GameBoard()
	ttt = TicTacToe(b, p1, p2)
	# p1.make_turn(0, b)
	# p1.make_turn(1, b)
	# p1.make_turn(2, b)
	ttt.play()

if __name__ == "__main__":

	main()