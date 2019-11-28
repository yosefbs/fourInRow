from enum import IntEnum
import numpy as np

class Color(IntEnum):
    NONE = 0
    RED = 1
    YELLOW = 2

class Board:
    def __init__(self):
        # a = np.arange(12)
        # B = a.reshape(3,4)
        # print(B)
        # print(B[:,1])
        #self.cells = [[' ']*7]*6
        self.cells = np.zeros([6,7],dtype=np.int)


    def printBoard(self):
        print(np.matrix(self.cells))

    def addToCol(self,colId: int,color: Color):
        col = self.cells[:,colId]
        rowId = np.where(col == int(Color.NONE))[0][-1]
        if color==Color.RED:
           print("red")
           self.cells[rowId,colId] = color.RED



