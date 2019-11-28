from Board import Board, Color

if __name__ == '__main__':
    b = Board()
    b.print_board()
    for i in range(4):
        #print(*(b.available_columns()))
        b.add_to_col(2,Color.RED)
        b.print_board()
        print()
    b.print_board()
    print()

