from board import GameBoard
from player import Player

def main():

	p1 = Player('x')
	g = GameBoard()

	p1.play(0, g)
	p1.play(1, g)
	p1.play(2, g)
	print(g.board)
	print(g._has_winner())

if __name__ == "__main__":

	main()