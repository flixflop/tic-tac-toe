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
	size = 5
	win = Window(w, h)
	x1, y1 = 20, 20
	cell_x, cell_y = (w - x1 * 2) / size, (h - y1 * 2) / size
	gb = GuiGameBoard(size, x1, y1, cell_x, cell_y, win)
	win.wait_for_close()



if __name__ == "__main__":

	main()