from tkinter import Tk, BOTH, Canvas

class ConsoleGameBoard:

	def __init__(self, size=3):
		self.size = size
		self.board = []
		self._create_board()

	def _create_board(self):
		for i in range(self.size):
			row = list(range(1 + i * self.size, self.size+1 + i * self.size))
			self.board.append(row)
			
	def render_board(self):
		for row in self.board:
			print(row)

class GuiGameBoard:

	def __init__(self, size, x1, y1, cellsize_x, cellsize_y, win):
		self.size = size
		self.board = []		
		self._x1 = x1
		self._y1 = y1
		self._cellsize_x = cellsize_x
		self._cellsize_y = cellsize_y
		self._win = win

		self._create_board()

	def _create_board(self):
		for i in range(self.size):
			row = []
			for j in range(self.size):
				row.append(Cell(self._win))
			self.board.append(row)

		for i in range(self.size):
			for j in range(self.size):
				c = self.board[i][j]
				self._draw_cell(i, j)

	def _draw_cell(self, i, j):
		
		if self._win is None:
			return
		
		top_left_x = self._x1 + i * self._cellsize_x
		top_left_y = self._y1 + j * self._cellsize_y
		bottom_right_x = self._x1 + (i + 1) * self._cellsize_x 
		bottom_right_y = self._y1 + (j + 1) * self._cellsize_y

		self.board[i][j].draw(top_left_x, top_left_y, bottom_right_x, bottom_right_y)
		self._animate()

	def _animate(self):

		if self._win is None:
			return

		self._win.redraw()
		#sleep(0.0)

class Window:

    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title("TicTacToe")
        self.__canvas = Canvas(self.__root, bg="white", height=height, width=width)
        self.__canvas.pack(fill=BOTH, expand=1)
        self.__running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.__running = True
        while self.__running:
            self.redraw()
        print("window closed...")

    def close(self):
        self.__running = False

    def draw_line(self, line, fill_color='blue'):
            line.draw(self.__canvas, fill_color=fill_color)

class Cell:
     
    def __init__(self, win=None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        # top left corner
        self._x1 = None
        self._y1 = None
        # bottom right corner
        self._x2 = None
        self._y2 = None
        self._win = win
        self.visited = False

    def draw(self, x1, y1, x2, y2):
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2
        
        if self.has_left_wall:
            line = Line(Point(x1, y1), Point(x1, y2))
            self._win.draw_line(line)
        else:
            line = Line(Point(x1, y1), Point(x1, y2))
            self._win.draw_line(line, fill_color='white')
        if self.has_right_wall:
            line = Line(Point(x2, y1), Point(x2, y2))
            self._win.draw_line(line)
        else:
            line = Line(Point(x2, y1), Point(x2, y2))
            self._win.draw_line(line, fill_color='white')
        if self.has_top_wall:
            line = Line(Point(x1, y1), Point(x2, y1))
            self._win.draw_line(line)
        else:
            line = Line(Point(x1, y1), Point(x2, y1))
            self._win.draw_line(line, fill_color='white')
        if self.has_bottom_wall:
            line = Line(Point(x1, y2), Point(x2, y2))
            self._win.draw_line(line)
        else:
            line = Line(Point(x1, y2), Point(x2, y2))
            self._win.draw_line(line, fill_color='white')

         

    def draw_move(self, to_cell, undo=False):
        if self._win is None:
            return
        x_mid = (self._x1 + self._x2) / 2
        y_mid = (self._y1 + self._y2) / 2

        to_x_mid = (to_cell._x1 + to_cell._x2) / 2
        to_y_mid = (to_cell._y1 + to_cell._y2) / 2

        fill_color = "red"
        if undo:
            fill_color = "gray"

        # moving left
        if self._x1 > to_cell._x1:
            line = Line(Point(self._x1, y_mid), Point(x_mid, y_mid))
            self._win.draw_line(line, fill_color)
            line = Line(Point(to_x_mid, to_y_mid), Point(to_cell._x2, to_y_mid))
            self._win.draw_line(line, fill_color)

        # moving right
        elif self._x1 < to_cell._x1:
            line = Line(Point(x_mid, y_mid), Point(self._x2, y_mid))
            self._win.draw_line(line, fill_color)
            line = Line(Point(to_cell._x1, to_y_mid), Point(to_x_mid, to_y_mid))
            self._win.draw_line(line, fill_color)

        # moving up
        elif self._y1 > to_cell._y1:
            line = Line(Point(x_mid, y_mid), Point(x_mid, self._y1))
            self._win.draw_line(line, fill_color)
            line = Line(Point(to_x_mid, to_cell._y2), Point(to_x_mid, to_y_mid))
            self._win.draw_line(line, fill_color)

        # moving down
        elif self._y1 < to_cell._y1:
            line = Line(Point(x_mid, y_mid), Point(x_mid, self._y2))
            self._win.draw_line(line, fill_color)
            line = Line(Point(to_x_mid, to_y_mid), Point(to_x_mid, to_cell._y1))
            self._win.draw_line(line, fill_color)

class Point:

	def __init__(self, x, y):
		self.x = x
		self.y = y


class Line:

    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def draw(self, canvas, fill_color):
        canvas.create_line(self.p1.x, self.p1.y, self.p2.x, self.p2.y, fill=fill_color, width=2)
        canvas.pack(fill=BOTH, expand=1)

