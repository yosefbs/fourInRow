import random

from Board import *


def calc_value_for_arr(arr: np.array, color: Color):
    repeated_in_row = 0
    max = 0
    empties = 0
    for cur in arr:
        if cur != color:
            if cur == Color.NONE:
                empties += 1
            repeated_in_row = 0
            continue
        repeated_in_row += 1
        if repeated_in_row > max:
            max = repeated_in_row
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

def calc_value_for_point(board : Board, col_id,row_id, color):
    value=0
    cells = np.array(board.cells,copy=True)
    cells[row_id,col_id]=color
    row = cells[row_id, :]
    value += calc_value_for_arr(row, color)

    col = cells[:, col_id]
    value += calc_value_for_arr(col, color)

    diag1 = np.diag(cells, k=col_id - row_id)
    value += calc_value_for_arr(diag1, color)

    diag2 = np.diag(np.fliplr(cells), k=(6 - col_id) - row_id)
    value += calc_value_for_arr(diag2, color)

    return value

class MachineLogicPlayer:
    def __init__(self, board: Board, color: Color):
        self.board = board
        self.color = color
        if color == Color.YELLOW:
            self.competitor_color=Color.RED
        else:
            self.competitor_color=Color.YELLOW
        return


    def play(self, avilable_col: list):
        my_value_vec = np.full((1, 7), -1)[0]
        competitor_value_vec=np.full((1, 7), -1)[0]
        for col_id in avilable_col:
            col = self.board.cells[:, col_id]
            free_in_col = np.where(col == int(Color.NONE))[0]
            row_id = free_in_col[-1]
            my_value_vec[col_id] = calc_value_for_point(self.board,col_id,row_id,self.color)
            competitor_value_vec[col_id] = calc_value_for_point(self.board,col_id,row_id,self.competitor_color)
        my_max = np.amax(my_value_vec)
        competitor_max=np.max(competitor_value_vec)
        if my_max < competitor_max:
            return np.argmax(competitor_value_vec)
        else:
            return np.argmax(my_value_vec)

class MachineRandomPlayer:
    def __init__(self, color: Color):
        self.color = color
        return

    def play(self, avilableCol: list):
        return random.choice(avilableCol)


class HumanPlayer:
    def __init__(self, color: Color):
        self.color = color

    def play(self, avilableCol: list):
        print('Select column\navailable columns: ',end='')
        print(*avilableCol)
        val = input()

        return val


class DebugPlayer:
    def __init__(self,color: Color):
        self.color = color
        self.step=-1
        self.moves= [5,6,0,2,6,4,6,6]

    def play(self, avilableCol: list):
        self.step+=1
        return self.moves[self.step]