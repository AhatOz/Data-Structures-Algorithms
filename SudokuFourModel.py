class SudokuFourModel:

    def __init__(self):
        self.__board = [[0 for i in range(4)] for j in range(4)]
        self.__locked = [[False for i in range(4)] for j in range(4)]
        self.__steps = 0

    def load_game(self, board, locked):
        self.__board = board
        self.__locked = locked

    def load_from_file(self, file):
        if not isinstance(file, str):
            raise TypeError("file should be a string")
        try:
            with open(file) as scanner:
                for i in range(0, 4):
                    line = scanner.readline().strip()
                    splits = line.split(",")
                    for j in range(0, 4):
                        digit = int(splits[j])
                        if digit < 0 or digit > 4:
                            raise ValueError("bad input file")
                        self.__board[i][j] = digit
                        if digit > 0:
                            self.__locked[i][j] = True
                        else:
                            self.__locked[i][j] = False
        except Exception as e:
            raise ValueError("bad input file")

    @property
    def board(self):
        return self.__board

    @property
    def locked(self):
        return self.__locked

    @property
    def steps(self):
        return self.__steps

    def check_puzzle(self):
        good = True
        for i in range(0, 4):
            good = good and self.check_row(i)
            good = good and self.check_column(i)
            good = good and self.check_region(i)
        return good

    def check_row(self, row):
        if not isinstance(row, int):
            raise TypeError("row is not an integer")
        if row < 0 or row > 3:
            raise ValueError("row is not between 0 and 3")
        for i in range(1, 5):
            found = False
            for j in range(0, 4):
                if self.__board[row][j] == i:
                    found = True
                    break
            if not found:
                return False
            found = False
        return True

    def check_column(self, column):
        if not isinstance(column, int):
            raise TypeError("column is not an integer")
        if column < 0 or column > 3:
            raise ValueError("column is not between 0 and 3")
        for i in range(1, 5):
            found = False
            for j in range(0, 4):
                if self.__board[j][column] == i:
                    found = True
                    break
            if not found:
                return False
            found = False
        return True

    def check_region(self, region):
        if not isinstance(region, int):
            raise TypeError("region is not an integer")
        if region < 0 or region > 3:
            raise ValueError("region is not between 0 and 3")
        row1 = 0
        row2 = 1
        col1 = 0
        col2 = 1
        if region == 1 or region == 3:
            col1 = 2
            col2 = 3
        if region == 2 or region == 3:
            row1 = 2
            row2 = 3
        for i in range(1, 5):
            if self.__board[row1][col1] == i or self.__board[row1][col2] == i \
                    or self.__board[row2][col1] == i \
                    or self.__board[row2][col2] == i:
                continue
            else:
                return False
        return True

    def prepare(self):
        for i in range(0, 4):
            for j in range(0, 4):
                if self.__board[i][j] == 0:
                    self.__board[i][j] = 1

    def solve(self):
        while not self.check_puzzle():
            self.solve_one_step()

    def solve_one_step(self):
        stop = False
        for i in range(0, 4):
            for j in range(0, 4):
                if self.__locked[i][j]:
                    continue
                if self.__board[i][j] >= 4:
                    self.__board[i][j] = 1
                    continue
                self.__board[i][j] += 1
                stop = True
                break
            if stop:
                break
        self.__steps += 1

    def recursive_solve(self):
        while not self.check_puzzle():
            self.recursive_solve_one_step()

    def recursive_solve_one_step(self):
        self.__steps += 1
        for i in range(len(self.__locked)):
            for j in range(len(self.__locked[i])):
                if not self.__locked[i][j]:
                    if self.__board[i][j] == 4:
                        self.__locked[i][j] = True
                        self.recursive_solve_one_step()
                        self.__locked[i][j] = False
                        self.__board[i][j] = 1
                        return
                    elif self.__board[i][j] < 4:
                        self.__board[i][j] += 1
                        return
                else:
                    continue