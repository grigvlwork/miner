from random import choice
from colorama import Fore, Back, Style


class Cell:
    def __init__(self, bomb=False, flag=0, is_opened=False):
        self.bomb = bomb
        self.flag = flag
        self.is_opened = is_opened
        self.bombs_around = None

    def __str__(self):
        if self.flag > 0:
            if self.flag == 1:
                return ('P')
            else:
                return ('?')
        else:
            if self.is_opened:
                if self.bomb and self.flag:
                    return 'X'
                if self.bomb:
                    return '*'
                return str(self.bombs_around)
            else:
                return '.'

    def __repr__(self):
        return self.__str__()

    def open(self):
        if not self.is_opened:
            if self.bomb:
                return -1
            else:
                self.is_opened = True
                return self.bombs_around
        else:
            return self.bombs_around

    def set_bomb(self):
        self.bomb = True


class Field(object):
    def __init__(self, rows, cols, bombs):
        self.rows = rows
        self.cols = cols
        self.bombs = bombs
        self.field = []
        for i in range(self.rows):
            row = []
            for j in range(self.cols):
                c = Cell()
                row.append(c)
            self.field.append(row)
        self.current_row = 0
        self.current_col = 0
        self.first_move = True
        self.game_over = False

    def change_flag(self):
        if not self.field[self.current_row][self.current_col].is_opened:
            self.field[self.current_row][self.current_col].flag = \
                (self.field[self.current_row][self.current_col].flag + 1) % 3

    def move_left(self):
        self.current_col = (self.current_col - 1) % self.cols

    def move_right(self):
        self.current_col = (self.current_col + 1) % self.cols

    def move_up(self):
        self.current_row = (self.current_row - 1) % self.rows

    def move_down(self):
        self.current_row = (self.current_row + 1) % self.rows

    def __str__(self):
        if self.game_over:
            self.open_all()
        rows = []
        for i in range(self.rows):
            if i == self.current_row and self.current_col == 0:
                row = "["
            else:
                row = " "
            for j in range(self.cols):
                row += str(self.field[i][j])
                if i == self.current_row and j == self.current_col:
                    row += "]"
                elif i == self.current_row and j == self.current_col - 1:
                    row += "["
                else:
                    row += " "
            if i == self.current_row and self.current_col == self.cols - 1:
                row += "]"
            else:
                row += " "
            rows.append(row)
        return "\n".join(rows)

    def __repr__(self):
        return self.__str__()

    def count_bombs(self, row, col):
        counter = 0
        for i in [-1, 0, 1]:
            for j in [-1, 0, 1]:
                if row + i in range(self.rows) and col + j in range(self.cols) and not (i == j == 0):
                    if self.field[row + i][col + j].bomb:
                        counter += 1
        return counter

    def generate(self):
        self.first_move = False
        # coords = list(range(self.rows * self.cols)).remove(self.current_row * self.cols + self.current_col)
        current = self.current_row * self.cols + self.current_col
        coords = list(range(self.rows * self.cols))
        coords.remove(current)
        bomb_coords = [choice(coords) for i in range(self.bombs)]
        for n in bomb_coords:
            row = n // self.cols
            col = n % self.cols
            self.field[row][col].set_bomb()
        for i in range(self.rows):
            for j in range(self.cols):
                if not self.field[i][j].bomb:
                    self.field[i][j].bombs_around = self.count_bombs(i, j)

    def draw(self):
        for c in self.__str__():
            if c == "1":
                print(Fore.LIGHTBLUE_EX + c, end="")
            elif c == "2":
                print(Fore.LIGHTGREEN_EX + c, end="")
            elif c == "3":
                print(Fore.LIGHTRED_EX + c, end="")
            elif c == "4":
                print(Fore.BLUE + c, end="")
            elif c == "5":
                print(Fore.RED + c, end="")
            elif c == "6":
                print(Fore.LIGHTMAGENTA_EX + c, end="")
            elif c == "7":
                print(Fore.GREEN + c, end="")
            elif c == "8":
                print(Fore.MAGENTA + c, end="")
            elif c == "P":
                print(Fore.GREEN + Back.LIGHTRED_EX + c, end="")
            elif c == ".":
                print(Fore.WHITE + c, end="")
            elif c == "*":
                print(Fore.BLACK + Back.LIGHTRED_EX + c, end="")
            elif c == "X":
                print(Fore.YELLOW + Back.LIGHTRED_EX + c, end="")
            else:
                print(c, end="")
            print(Style.RESET_ALL, end="")
        print()

    def open(self):
        if self.game_over:
            return
        if self.first_move:
            self.generate()
        if self.field[self.current_row][self.current_col].bomb:
            self.game_over = True
            self.open_all()
            return
        if self.field[self.current_row][self.current_col].is_opened:
            return
        cells_to_open = [self.current_row * self.cols + self.current_col]
        while len(cells_to_open) > 0:
            n = cells_to_open.pop(0)
            row = n // self.cols
            col = n % self.cols
            self.field[row][col].is_opened = True
            if self.field[row][col].bombs_around == 0:
                for i in [-1, 0, 1]:
                    for j in [-1, 0, 1]:
                        if row + i in range(self.rows) and col + j in range(self.cols) and not (i == j == 0):
                            if not self.field[row + i][col + j].is_opened:
                                cells_to_open.append((row + i) * self.cols + col + j)

    def open_all(self):
        for i in range(self.rows):
            for j in range(self.cols):
                self.field[i][j].is_opened = True
