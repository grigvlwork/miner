class Cell:
    def __init__(self, bomb=False, flag=0, is_opened=False):
        self.bomb = bomb
        self.flag = flag
        self.is_opened = is_opened
        self.bombs_around = None

    def __str__(self):
        if self.flag > 0:
            if self.flag == 1:
                return('P')
            else:
                return('?')
        else:
            if self.is_opened:
                return str(self.bombs_around)
            else:
                return '.'

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
        self.field = [[Cell()] * self.cols for x in range(self.rows)]
        self.current_row = 0
        self.current_col = 0
        self.first_move = True

    def __str__(self):
        rows = []
        for i in range(self.rows):
            row = ""
            for j in range(self.cols):
                if i == self.current_row and j == self.current_col:
                    row += "[" + str(self.field[i][j]) + "]"
            rows.append(row)
        return "\n".join(rows)





