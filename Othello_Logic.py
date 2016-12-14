#Jason Zhan Chen ID# 34461315
class InvalidMoveError(Exception):
    pass
class GameOverException(Exception):
    pass

class OthelloGameState:
    def __init__(self,row_input,column_input,top_left_input,turn_input,rule_input):
        self.board = []
        self.row = row_input
        self.column = column_input
        self.top_left = top_left_input
        self.turn = turn_input
        self.rule = rule_input
    
    def board_creation(self):
        board =[]
        for x in range(int(self.row)):
            board.append(['.'] * int(self.column))
        if self.top_left == 'B':
            board[int((int(self.row)/2)-1)][int((int(self.column)/2)-1)] = 'B'
            board[int((int(self.row)/2)-1)][int((int(self.column)/2))] = 'W'
            board[int((int(self.row)/2))][int((int(self.column)/2)-1)] = 'W'
            board[int((int(self.row)/2))][int((int(self.column)/2))] = 'B'
        elif self.top_left == 'W':
            board[int((int(self.row)/2)-1)][int((int(self.column)/2)-1)] = 'W'
            board[int((int(self.row)/2)-1)][int((int(self.column)/2))] = 'B'
            board[int((int(self.row)/2))][int((int(self.column)/2)-1)] = 'B'
            board[int((int(self.row)/2))][int((int(self.column)/2))] = 'W'
        self.board = board
    
    def invalid_cell(self,move_coordinates):
        if (int(self.row)-1) < move_coordinates[0] or move_coordinates[0] < 0:
            return True
        if (int(self.column)-1) < move_coordinates[1] or move_coordinates[1] < 0:
            return True
        return False
        
    def invalid_move(self,move_coordinates):
        if self.board[move_coordinates[0]][move_coordinates[1]] != '.':
            return True
        return False

    def move_coordinates(self, move_input):
        move_coordinates = move_input.split(' ')
        move_coordinates = ((int(move_coordinates[0])-1),(int(move_coordinates[1])-1))
        return move_coordinates
        
    def place_a_piece(self, move_coordinates):
        if self.turn == 'B':
                self.board[move_coordinates[0]][move_coordinates[1]] = 'B'
        elif self.turn == 'W':
            self.board[move_coordinates[0]][move_coordinates[1]] = 'W'

    def turn_opposite(self):
        if self.turn == 'B':
            self.turn = 'W'
        elif self.turn == 'W':
            self.turn = 'B'
        return self.turn

    def color_count(self):
        self.black_counter = 0
        self.white_counter = 0
        for row in self.board:
            for x in row:
                if x == 'B':
                    self.black_counter += 1
                elif x == 'W':
                    self.white_counter += 1
        return('B: '+str(self.black_counter)+' W: '+str(self.white_counter))

    def win(self):
        if self.rule == '<':
            if self.white_counter < self.black_counter:
                return('White Wins')
            elif self.white_counter > self.black_counter:
                return('Black Wins')
            elif self.white_counter == self.black_counter:
                return('No Winner')
        if self.rule == '>':
            if self.white_counter < self.black_counter:
                return('Black Wins')
            elif self.white_counter > self.black_counter:
                return('White Wins')
            elif self.white_counter == self.black_counter:
                return('No Winner')
            
    def move(self,move_coordinates,row_increment,column_increment,opposite_color_to_flip):
        direction_flip = []
        row_index = move_coordinates[0]
        column_index = move_coordinates[1]
        while not self.invalid_cell((row_index,column_index)):
            row_index += row_increment
            column_index += column_increment
            if self.invalid_cell((row_index,column_index)):
                break
            if self.turn == 'B':
                if self.board[row_index][column_index] == 'W':
                    direction_flip.append((row_index,column_index))
                elif self.board[row_index][column_index] == 'B':
                    for cell in direction_flip:
                        opposite_color_to_flip.append(cell)
                    break
                elif self.board[row_index][column_index] == '.':
                    break
            elif self.turn == 'W':
                if self.board[row_index][column_index] == 'B':
                    direction_flip.append((row_index,column_index))
                elif self.board[row_index][column_index] == 'W':
                    for cell in direction_flip:
                        opposite_color_to_flip.append(cell)
                    break
                elif self.board[row_index][column_index] == '.':
                    break
        return opposite_color_to_flip

    def all_move(self,move_coordinates):
        opposite_color_to_flip = []
        opposite_color_to_flip.extend(self.move(move_coordinates,1,0,opposite_color_to_flip))
        opposite_color_to_flip.extend(self.move(move_coordinates,-1,0,opposite_color_to_flip))
        opposite_color_to_flip.extend(self.move(move_coordinates,0,1,opposite_color_to_flip))
        opposite_color_to_flip.extend(self.move(move_coordinates,0,-1,opposite_color_to_flip))
        opposite_color_to_flip.extend(self.move(move_coordinates,1,1,opposite_color_to_flip))
        opposite_color_to_flip.extend(self.move(move_coordinates,1,-1,opposite_color_to_flip))
        opposite_color_to_flip.extend(self.move(move_coordinates,-1,1,opposite_color_to_flip))
        opposite_color_to_flip.extend(self.move(move_coordinates,-1,-1,opposite_color_to_flip))
        return opposite_color_to_flip
    
    def flip(self,move_coordinates):
        if self.board[move_coordinates[0]][move_coordinates[1]] != '.':
            return False
        valid = False
        opposite_color_to_flip = self.all_move(move_coordinates)
        if self.turn == 'B':
            for cell in opposite_color_to_flip:
                valid = True
                row = cell[0]
                column = cell[1]
                self.board[row][column] = 'B'
        elif self.turn == 'W':
            for cell in opposite_color_to_flip:
                valid = True
                row = cell[0]
                column = cell[1]
                self.board[row][column] = 'W'
        return valid
    
    def location_of_pieces(self, player):
        location_list = []
        for row in range(len(self.board)):
            for cell in range(len(self.board[row])):
                if self.board[row][cell] == player:
                    location_list.append((row,cell))
        return location_list

    def any_move(self):
        avaliable_moves = []
        list_of_locations = self.location_of_pieces('.')
        for cell in list_of_locations:
                move_row = cell[0]
                move_column = cell[1]
                move_coordinates = (move_row,move_column)
                opposite_color_to_flip = self.all_move(move_coordinates)
                if opposite_color_to_flip != []:
                    avaliable_moves.extend(opposite_color_to_flip)
                else:
                    pass
        if avaliable_moves == []:
            self.turn_opposite()
        else:
            pass
        return avaliable_moves

    
    def game_over_check(self):
        avaliable_moves = self.any_move()
        if avaliable_moves != []:
            return
        avaliable_moves = self.any_move()
        if avaliable_moves != []:
            return
        return True

    def print_board(self):
        for row in range(len(self.board)):
            for column in range(len(self.board[row])):
                print(self.board[row][column], end = ' ')
            print()
                
