from enum import IntEnum

import numpy as np


class Color(IntEnum):
    NONE = 0
    RED = 1
    YELLOW = 2


def check_for_4(arr : np.array,color:Color):
    repeated_in_row=0
    for cur in arr:
        if cur != color:
            repeated_in_row = 0
            continue
        repeated_in_row += 1
        if repeated_in_row == 4:
            return True
    return False


class Board:
    def __init__(self):
        # a = np.arange(12)
        # B = a.reshape(3,4)
        # print(B)
        # print(B[:,1])
        # self.cells = [[' ']*7]*6
        self._game_complete =False
        self.cells = np.zeros([6, 7], dtype=np.int)
        self._winner= Color.NONE

    @property
    def winner(self):
        return self._winner

    def print_board(self):
        print(np.matrix(self.cells))

    def __check_for_winner(self,row_id,col_id,color:Color):
        color = Color(self.cells[row_id, col_id])
        row = self.cells[row_id, :]
        win = check_for_4(row,color)
        if not win:
            col = self.cells[:, col_id]
            win = check_for_4(col, color)
            if not win:
                col = self.cells[:, col_id]
                win = check_for_4(col, color)

        if win:
            self._winner = color
            self._game_complete = True
            return True
        return False

    def add_to_col(self, col_id: int, color: Color):
        col = self.cells[:, col_id]
        free_in_col= np.where(col == int(Color.NONE))[0]
        if len(free_in_col) == 0:
            return
        row_id = free_in_col[-1]
        if color == Color.RED:
            self.cells[row_id, col_id] = color.RED
        elif color == Color.YELLOW:
            self.cells[row_id, col_id] = color.YELLOW
        self.__check_for_winner(row_id,col_id,color)

    def available_columns(self)->list:
        first_row = self.cells[0,:]
        return np.where(first_row == int(Color.NONE))


