from Board import Board, Color
from GameEngine import GameEngine
from player import *

if __name__ == '__main__':
    b = Board()
    p1 = MachineLogicPlayer(b,Color.RED)
    p2 = MachineRandomPlayer(Color.YELLOW)
    eng = GameEngine()
    # eng.denug_play_game(b)
    eng.play_game(b,p1,p2)
    b.print_board()

    #
    # b.print_board()
    # for i in range(4):
    #     #print(*(b.available_columns()))
    #     b.add_to_col(2,Color.RED)
    #     b.print_board()
    #     print()
    # b.print_board()
    print()

