from window import Window
from maze import Maze


def main():
    win = Window(800, 600)

    num_rows = 12
    num_cols = 16
    margin = 50
    cell_size_x = 40
    cell_size_y = 40

    maze = Maze(margin, margin, num_rows, num_cols, cell_size_x, cell_size_y, win)

    solved = maze.solve()
    print("Maze solved!" if solved else "Maze could not be solved.")

    win.wait_for_close()


if __name__ == "__main__":
    main()
