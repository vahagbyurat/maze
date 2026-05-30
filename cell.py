from graphics import Point, Line


class Cell:
    def __init__(self, win=None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.__x1 = -1.0
        self.__x2 = -1.0
        self.__y1 = -1.0
        self.__y2 = -1.0
        self.__win = win
        self.visited = False

    def draw(self, x1, y1, x2, y2):
        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2

        if self.__win is None:
            return

        bg = "#d9d9d9"

        left = Line(Point(self.__x1, self.__y1), Point(self.__x1, self.__y2))
        self.__win.draw_line(left, "black" if self.has_left_wall else bg)

        top = Line(Point(self.__x1, self.__y1), Point(self.__x2, self.__y1))
        self.__win.draw_line(top, "black" if self.has_top_wall else bg)

        right = Line(Point(self.__x2, self.__y1), Point(self.__x2, self.__y2))
        self.__win.draw_line(right, "black" if self.has_right_wall else bg)

        bottom = Line(Point(self.__x1, self.__y2), Point(self.__x2, self.__y2))
        self.__win.draw_line(bottom, "black" if self.has_bottom_wall else bg)

    def draw_move(self, to_cell, undo=False):
        if self.__win is None:
            return

        self_center = Point(
            (self.__x1 + self.__x2) / 2,
            (self.__y1 + self.__y2) / 2,
        )
        to_center = Point(
            (to_cell.__x1 + to_cell.__x2) / 2,
            (to_cell.__y1 + to_cell.__y2) / 2,
        )

        fill_color = "gray" if undo else "red"
        self.__win.draw_line(Line(self_center, to_center), fill_color)
