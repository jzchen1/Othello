import Othello_Logic
#Jason Zhan Chen ID# 34461315
def game():
    row_input =input()
    column_input =input()
    top_left_input =input()
    turn_input =input()
    rule_input =input()
    gamestate = Othello.OthelloGameState(row_input,column_input,top_left_input,turn_input,rule_input)
    gamestate.board_creation()
    while True:
        move_input = input()
        try:
            move_coordinate = gamestate.move_coordinates(move_input)
            valid_move = gamestate.flip(move_coordinate)
            if valid_move:
                gamestate.place_a_piece(move_coordinate)
                gamestate.turn_opposite()
                print("VALID")
            else:
                raise Exception
        except:
            print("INVALID")
        gamestate.game_over_check()
        print(gamestate.color_count())
        gamestate.print_board()
if __name__ == '__main__':
    game()
