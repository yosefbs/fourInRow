from Board import Board, Color

if __name__ == '__main__':
    b = Board()
    b.printBoard()
    b.addToCol(2,Color.RED)
    b.printBoard()
    print()

