#Jason Zhan Chen ID# 34461315
import tkinter
import Othello_Logic

class InputWindow:
    def __init__(self):
        self.input_window = tkinter.Toplevel()
        row_label = tkinter.Label(master = self.input_window, text = 'How many rows?',font = ('Helvetica', 14))
        row_label.grid(row = 0, column = 0, padx = 10, pady = 10,sticky = tkinter.W)        
        self.row_entry = tkinter.Entry(master = self.input_window, width = 20, font = ('Helvetica', 14))
        self.row_entry.grid(row = 0, column = 1, padx = 10, pady = 1,sticky = tkinter.W + tkinter.E)
        column_label = tkinter.Label(master = self.input_window, text = 'How many columns?',font = ('Helvetica', 14))
        column_label.grid(row = 1, column = 0, padx = 10, pady = 10,sticky = tkinter.W)        
        self.column_entry = tkinter.Entry(master = self.input_window, width = 20, font = ('Helvetica', 14))
        self.column_entry.grid(row = 1, column = 1, padx = 10, pady = 1,sticky = tkinter.W + tkinter.E)
        first_label = tkinter.Label(master = self.input_window, text = 'Who goes first?',font = ('Helvetica', 14))
        first_label.grid(row = 2, column = 0, padx = 10, pady = 10,sticky = tkinter.W)        
        self.first_entry = tkinter.Entry(master = self.input_window, width = 20, font = ('Helvetica', 14))
        self.first_entry.grid(row = 2, column = 1, padx = 10, pady = 1,sticky = tkinter.W + tkinter.E)
        top_left_label = tkinter.Label(master = self.input_window, text = 'What color in top left?',font = ('Helvetica', 14))
        top_left_label.grid(row = 3, column = 0, padx = 10, pady = 10,sticky = tkinter.W)        
        self.top_left_entry = tkinter.Entry(master = self.input_window, width = 20, font = ('Helvetica', 14))
        self.top_left_entry.grid(row = 3, column = 1, padx = 10, pady = 1,sticky = tkinter.W + tkinter.E)
        rule_label = tkinter.Label(master = self.input_window, text = 'Determine winner by less than or greater than?',font = ('Helvetica', 14))
        rule_label.grid(row = 4, column = 0, padx = 10, pady = 10,sticky = tkinter.W)        
        self.rule_entry = tkinter.Entry(master = self.input_window, width = 20, font = ('Helvetica', 14))
        self.rule_entry.grid(row = 4, column = 1, padx = 10, pady = 1,sticky = tkinter.W + tkinter.E)
        button_frame = tkinter.Frame(master = self.input_window)
        button_frame.grid(row = 5, column = 0, columnspan = 2, padx = 10, pady = 10,sticky = tkinter.E + tkinter.S)
        create_board_button = tkinter.Button(master = button_frame, text = 'Create Board', font = ('Helvetica', 14),command = self.on_create_board_button)
        create_board_button.grid(row = 0, column = 0, padx = 10, pady = 10)
        self.input_window.rowconfigure(5, weight = 1)
        self.input_window.columnconfigure(1, weight = 1)
        self.create_board_clicked = False
        self.row = ''
        self.column = ''
        self.first = ''
        self.top_left = ''
        self.rule = ''

    def show(self):
        self.input_window.grab_set()
        self.input_window.wait_window()

    def was_create_board_clicked(self):
        return self.create_board_clicked

    def get_row(self):
        return self.row

    def get_column(self):
        return self.column

    def get_first(self):
        return self.first

    def get_top_left(self):
        return self.top_left

    def get_rule(self):
        return self.rule

    def on_create_board_button(self):
        self.create_board_clicked = True
        self.row = self.row_entry.get()
        self.column = self.column_entry.get()
        self.first = self.first_entry.get()
        self.top_left = self.top_left_entry.get()
        self.rule = self.rule_entry.get()
        self.input_window.destroy()   
        
class GUI:
    def __init__(self):
        inputs = InputWindow()
        inputs.show()
        self.row_input = inputs.get_row()
        self.column_input = inputs.get_column()
        self.top_left_input = inputs.get_top_left()
        self.turn_input = inputs.get_first()
        self.rule_input = inputs.get_rule()
        self.window = tkinter.Tk()
        self.canvas = tkinter.Canvas(master = self.window, width = 400, height = 400,background = '#001050')
        self.canvas.bind('<Button-1>', self.place_a_piece)
        self.canvas.grid(row = 1, column = 0,columnspan = 4, padx = 0, pady=10,sticky = tkinter.N + tkinter.S + tkinter.W + tkinter.E)
        self.window.rowconfigure(1, weight = 10)
        self.window.columnconfigure(0, weight = 1)
        self.window.columnconfigure(1, weight = 10)
        self.window.columnconfigure(2, weight = 100)
        self.window.columnconfigure(3, weight = 1000)
        self.list_of_pieces = []
        self.gamestate = Othello.OthelloGameState(self.row_input,self.column_input,self.top_left_input,self.turn_input,self.rule_input)
        self.gamestate.board_creation()
        self.gamestate.color_count()
        self.canvas.bind('<Configure>', self.resize)
        
    def start(self):
        self.window.mainloop()
        
    def create_board(self):
        self.canvas_width = self.canvas.winfo_width()
        self.canvas_height = self.canvas.winfo_height()
        self.coordinate_list = []
        for rows in range(int(self.row_input)):
            sub_list = []
            y_coordinate_1 = (self.canvas_height/int(self.row_input)*rows)/self.canvas_height
            y_coordinate_2 = (self.canvas_height/int(self.row_input)*(rows+1))/self.canvas_height
            for columns in range(int(self.column_input)):
                x_coordinate_1 = (self.canvas_width/int(self.column_input)*columns)/self.canvas_width
                x_coordinate_2 = (self.canvas_width/int(self.column_input)*(columns+1))/self.canvas_width
                sub_list.append((x_coordinate_1,y_coordinate_1,x_coordinate_2,y_coordinate_2))
                self.canvas.create_rectangle((x_coordinate_1*self.canvas_width),(y_coordinate_1*self.canvas_height),(x_coordinate_2*self.canvas_width),(y_coordinate_2*self.canvas_height))
            self.coordinate_list.append(sub_list)

    def place_a_piece(self,event: tkinter.Event):
        self.x_coordinate = event.x
        self.y_coordinate = event.y
        self.grid_width = self.canvas.winfo_width() / int(self.column_input)
        self.grid_length = self.canvas.winfo_height() / int(self.row_input)
        self.row_index = int(event.y//self.grid_length)
        self.column_index = int(event.x//self.grid_width)
        try:
            valid_move = self.gamestate.flip((self.row_index,self.column_index))
            if valid_move:
                for sublist in self.coordinate_list:
                    for rectangle in sublist:
                        if rectangle[0]*self.canvas_width <= self.x_coordinate < rectangle[2]*self.canvas_width and rectangle[1]*self.canvas_height <= self.y_coordinate < rectangle[3]*self.canvas_height:
                            self.canvas.create_oval(rectangle[0]*self.canvas_width,rectangle[1]*self.canvas_height,rectangle[2]*self.canvas_width,rectangle[3]*self.canvas_height)
                            coordinate = (rectangle[0],rectangle[1],rectangle[2],rectangle[3])
                            self.list_of_pieces.append(coordinate)
                self.gamestate.place_a_piece((self.row_index,self.column_index))
                self.gamestate.turn_opposite()
                self.canvas.delete(tkinter.ALL)
                self.create_board()
                self.draw_black_piece()
                self.draw_white_piece()
                self.gamestate.color_count()
                self.gameover = self.gamestate.game_over_check()
                if self.gameover == True:
                    self.winner_counter = tkinter.Label(master=self.window, text = 'Winner:'+' '+str(self.gamestate.win()),font = ('Helvetica', 8))
                    self.winner_counter.grid(row = 0, column= 3, padx = 10, pady = 10, sticky = tkinter.W)
                self.white_counter = tkinter.Label(master=self.window, text = 'White:'+' '+str(self.gamestate.white_counter),font = ('Helvetica', 8))
                self.white_counter.grid(row = 0, column= 2, padx = 10, pady = 10, sticky = tkinter.W)
                self.black_counter = tkinter.Label(master=self.window, text = 'Black:'+' '+str(self.gamestate.black_counter),font = ('Helvetica', 8))
                self.black_counter.grid(row = 0, column= 1, padx = 10, pady = 10, sticky = tkinter.W)
                self.turn_counter = tkinter.Label(master=self.window, text = 'Turn:'+' '+str(self.gamestate.turn),font = ('Helvetica', 8))
                self.turn_counter.grid(row = 0, column= 0, padx = 10, pady = 10, sticky = tkinter.W)
            else:
                raise Exception
        except:
            pass
        return self.list_of_pieces
        

    def draw_piece(self,piece):
        self.canvas_width = self.canvas.winfo_width()
        self.canvas_height = self.canvas.winfo_height()
        self.canvas.create_oval(self.canvas_width * piece[0], self.canvas_height * piece[1],self.canvas_width * piece[2], self.canvas_height * piece[3])
        
    def draw_pieces(self, list_of_pieces):
        for piece in list_of_pieces:
            self.draw_piece(piece)
        
    def resize(self,event: tkinter.Event):
        self.canvas.delete(tkinter.ALL)
        self.create_board()
        self.draw_black_piece()
        self.draw_white_piece()
        self.white_counter = tkinter.Label(master=self.window, text = 'White:'+' '+str(self.gamestate.white_counter),font = ('Helvetica', 8))
        self.white_counter.grid(row = 0, column= 2, padx = 10, pady = 10, sticky = tkinter.W)
        self.black_counter = tkinter.Label(master=self.window, text = 'Black:'+' '+str(self.gamestate.black_counter),font = ('Helvetica', 8))
        self.black_counter.grid(row = 0, column= 1, padx = 10, pady = 10, sticky = tkinter.W)
        self.turn_counter = tkinter.Label(master=self.window, text = 'Turn:'+' '+str(self.gamestate.turn),font = ('Helvetica', 8))
        self.turn_counter.grid(row = 0, column= 0, padx = 10, pady = 10, sticky = tkinter.W)
        
    def draw_black_piece(self):
        location_list = self.gamestate.location_of_pieces('B')
        for black in location_list:
            row_index = black[0]*self.canvas.winfo_height()/int(self.row_input)
            column_index = black[1]*self.canvas.winfo_width()/int(self.column_input)
            self.canvas.create_oval(column_index,row_index,(column_index+(self.canvas.winfo_width()/int(self.column_input))),(row_index+(self.canvas.winfo_height()/int(self.row_input))), fill='black')

    def draw_white_piece(self):
        location_list = self.gamestate.location_of_pieces('W')
        for white in location_list:
            row_index = white[0]*self.canvas.winfo_height()/int(self.row_input)
            column_index = white[1]*self.canvas.winfo_width()/int(self.column_input)
            self.canvas.create_oval(column_index,row_index,(column_index+(self.canvas.winfo_width()/int(self.column_input))),(row_index+(self.canvas.winfo_height()/int(self.row_input))), fill='white')

if __name__ == '__main__':
    gui = GUI()
    gui.start()

