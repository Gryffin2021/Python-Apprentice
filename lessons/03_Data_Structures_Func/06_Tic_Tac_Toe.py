#imports
from guizero import App, Box, PushButton, Text, info

X_MARK = "X"
O_MARK = "O"

# Implement check_row() and check_win() to allow the game to check if a player has won
# IMPORTANT! In your code, you should use the constants X_MARK and O_MARK instead of the strings "x" and "o"
board = 0
def transpose(a):
    return list(zip(*a)) 

def check_row(r):
    """Check if a player won on a row
    Args:
        l: a 3 element iterable
        
    Returns:
        The winner's token ( x or o ) if there is one, otherwise None
        """
    if all([e == X_MARK for e in r]):
        return X_MARK
    elif all([e == O_MARK for e in r]):
        return O_MARK
    else:
        return None

def check_col(c):   
    if all([e == X_MARK for e in c]):
        return X_MARK
    elif all([e == O_MARK for e in c]):
        return O_MARK
    else:
        return None
        
def check_d(board):

    d1 = [ board[i][i] for i in range(3) ]
    d2 = [ board[i][2-i] for i in range(3) ]
    if(d1 == [O_MARK, O_MARK, O_MARK]):
        return O_MARK
    elif(d2 == [X_MARK, X_MARK, X_MARK]):
        return X_MARK
    elif(d1 == [O_MARK, O_MARK, O_MARK]):
        return O_MARK
    elif(d2 == [O_MARK, O_MARK, O_MARK]):
        return O_MARK
    else:
        return None
    

m = board[:] # Copy the whole list 
m.extend(transpose(board)) # Add all of the items from transpose to m, a bit like m += transpose(l)
def check_win(board):
    for i in range(1, len(m)):
        if(i == 1 or i == 4 or i == 7):
            if(m[i] == X_MARK and m[i+1] == X_MARK and m[i+2] == X_MARK):
                return X_MARK
        if(i == 1 or i == 2 or i == 3):
            if(m[i] == X_MARK and m[i+3] == X_MARK and m[i+6] == X_MARK):
                return X_MARK
        if(i == 1):
            if(m[i] == X_MARK and m[i+4] == X_MARK and m[i+8]):
                return X_MARK
        if(i == 3):
            if(m[i+2] == X_MARK and m[i+4] == X_MARK and m[i+6] == X_MARK):
                return X_MARK
        
        if(i == 1 or i == 4 or i == 7):
            if(m[i] == O_MARK and m[i+1] == O_MARK and m[i+2] == O_MARK):
                return O_MARK
        if(i == 1 or i == 2 or i == 3):
            if(m[i] == O_MARK and m[i+3] == O_MARK and m[i+6] == O_MARK):
                return O_MARK
        if(i == 1):
            if(m[i] == O_MARK and m[i+4] == O_MARK and m[i+8]):
                return O_MARK
        if(i == 3):
            if(m[i+2] == O_MARK and m[i+4] == O_MARK and m[i+6] == O_MARK):
                return O_MARK
    return None
        

# The following code is the main part of the program. It creates a GUI for the
# game and handles the game logic. Implement the functions above first, then
# after your program is working you can try chaning the code below. 

class TicTacToe:
    """A Simple Tic Tac Toe game"""

    app = None
    board = None # The storage for user's markers
    buttons = None # Holds UI elements for the board
    board_pane = None #
    message = None
    turn_n = 0
    turn = X_MARK

    def __init__(self, win_func=check_win):
        self.board = None # The stoage for user's markers
        
        self.app = App('Tic Tac Toe Game', bg='burlywood')
        self.board_pane = Box(self.app, layout='grid') # Holds UI elements for the board     
        self.message = Text(self.app, text="It is your turn, " + self.current_turn)

        self.reset_button = PushButton(self.app, text='Reset', command=self.reset)

        self.message.text_color = "green"

        self.win_func = win_func

        self.reset()

    def reset(self):
        """Reset the game state"""
        self.turn_n = 0
        self.turn = X_MARK
        self.message.value = "It's your turn, " + self.current_turn
        
        self.board   = [[None for _ in range(3)] for _ in range(3)]
        self.buttons = [[None for _ in range(3)] for _ in range(3)]

        # generate a 3x3 grid
        for x in range(3):
            for y in range(3):
                self.buttons[x][y] = PushButton(self.board_pane, text='', grid=[x, y], width=3, command=self.do_turn, args=[x,y])

    def start(self):
        """Start the game"""
        self.app.display()

    @property
    def current_turn(self):
        """Return the current player's marker, based on the current turn number"""
        return [X_MARK, O_MARK][self.turn_n % 2]

    def do_turn(self, x, y):
        """Handle one player turn, and return a marker if one of the players won"""
        self.board[x][y] = self.current_turn
        self.buttons[x][y].text = self.current_turn
        self.buttons[x][y].disable()

        self.turn_n += 1
        self.message.value = f"It's your turn, {self.current_turn}"

        winner = self.win_func(self.board)

        if winner:
            self.message.value = f"Player {winner} won!"
            info("Tic-tac-toe",f"Player {winner} won!")
            for row in self.buttons:
                for button in row:
                    button.disable()
        elif self.turn_n == 9:
            self.message.value = "It's a draw!"
            info("Tic-tac-toe","It's a draw!")

ttt = TicTacToe(check_win)
ttt.start()
