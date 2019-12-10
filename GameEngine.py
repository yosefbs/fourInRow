class GameEngine:

    def play_game(self,board,player1,player2,print_moves=False):
        win = False
        while True:
            selectedCol = player1.play(board.available_columns())
            win = board.add_to_col(selectedCol,player1.color)
            if win:
                break
            selectedCol = player2.play(board.available_columns())
            win = board.add_to_col(selectedCol, player2.color)
            if win or len(board.available_columns())==0:
                break
            if print_moves:
                board.print_board()
                print()
        print('The winner is: ',end='')
        print(board.winner)
        return

    def denug_play_game(self, board ):
        win = False
        red_stepssss = [2,3,6,2,3,4,1,6,2,6,1,2]
        yellow_steps = [0,1,4,5,0,1,6,2,1,6,1,0]
        for i in range(len(red_stepssss)):
            from Board import Color
            win = board.add_to_col(red_stepssss[i], Color.RED)
            if win:
                break
            win = board.add_to_col(yellow_steps[i], Color.YELLOW)
            if win or len(board.available_columns()) == 0:
                break
            board.print_board()
            print()
        print('The winner is: {0}'.format(board.winner))
        return