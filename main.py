from board import ConsoleGameBoard, GuiGameBoard, Window, Line, Point
from player import Player
from tictactoe import TicTacToe

def main():

	# gb = GameBoard(size=5)
	# print(gb.board)

	# p1 = Player('x')
	# p2 = Player('o')
	# b = GameBoard(size=4)
	# ttt = TicTacToe(b, p1, p2)

	# ttt.play()
	w, h = 600, 600
	win = Window(w, h)
	gb = GuiGameBoard(3, 20, 20, 50, 50, win)
	win.wait_for_close()



if __name__ == "__main__":

	main()