import random

from Board import *


class MachineLogicPlayer:
    def __init__(self, board: Board, color: Color):
        self.board = board
        self.color = color
        return

    def calc_value_for_arr(self, arr: np.array, color: Color):
        repeated_in_row = 0
        max = 0
        empties = 0
        for cur in arr:
            if cur != color:
                if cur == Color.NONE:
                    empties += 1
                if repeated_in_row > max:
                    max = repeated_in_row
                repeated_in_row = 0
                continue
            repeated_in_row += 1
            if repeated_in_row == 4:
                break

        if max == 2 and empties > 2:
            return 1
        elif max == 3 and empties > 0:
            return 6
        elif max == 4:
            return 100
        else:
            return 0

    def calc_values(self, col_id, color):
        col = self.board.cells[:, col_id]
        free_in_col = np.where(col == int(Color.NONE))[0]
        row_id = free_in_col[-1]

        value=0
        row = self.cells[row_id, :]
        value += self.calc_value_for_arr(row, color)

        col = self.cells[:, col_id]
        value +=  self.calc_value_for_arr(col, color)

        diag1 = np.diag(self.cells, k=col_id - row_id)
        value += self.calc_value_for_arr(diag1, color)

        diag2 = np.diag(np.fliplr(self.cells), k=(6 - col_id) - row_id)
        value += self.calc_value_for_arr(diag2, color)

        return value

    def play(self, avilableCol: list):
        my_value_vec = np.zeros(7)
        for col_id in avilableCol:
            my_value_vec[col_id] = self.calc_values(col_id,self.color)
        return random.choice(avilableCol)


class MachineRandomPlayer:
    def __init__(self, color: Color):
        self.color = color
        return

    def play(self, avilableCol: list):
        return random.choice(avilableCol)


class HumanPlayer:
    def __init__(self, color: Color):
        self.color = color
        return

    def play(self, avilableCol: list):
        print('select column to insert coin\navailable columns: {0}'.format(*avilableCol))
