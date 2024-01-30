from player import HumanPlayer, RandomComputerPlayer

class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)] # we will use a single list to rep 3*3 board
        self.current_winner = None # keep track of the winner
    
    def print_board(self):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')
    
    def print_board_nums():
        number_board = [[str(i) for i in range(j*3,(j+1)*3)] for j in range(3)]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')
            
    def available_moves(self):
        #return []
        moves = [] # initialize an empty list to store the indices of available moves
        for (i, spot) in enumerate(self.board): # enumerate gives index and value at that index
            #example ['x', 'x', 'o'] --> [(0, 'x'), (1, 'x'), (2, 'o') ]
            if spot == ' ':
                moves.append(i)
        return moves        
    
    def empty_squares(self):
        return ' ' in self.board
    
    def num_empty_spaces(self):
        return self.board.count(' ')
    
    def make_move(self, square, letter):
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        
        return False
    
    def winner(self, square, letter):
        #winner is 3 in a row anywhere (row, column, diagonal)
        row_ind = row // 3
        row = self.board[row_ind*3: (row_ind + 1)* 3]
        if all([spot == letter for spot in row]):
            return True
        
        #check column
        col_ind = square % 3
        column = [self.board[col_ind + i *3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True
        
        #check diagonals
        #to win a diagonal, only moves possible are 0,2,4,6,8
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0,4,8]]
            if all([spot == letter for spot in diagonal1]):
                return True
            diagonal1 = [self.board[i] for i in [2,4,6]]
            if all([spot == letter for spot in diagonal2]):
                return True
        
        #if all the above checks fail
        return False 
        
        
def play(game, x_player, o_player, print_game=True):
    #returns the winner for a game or none for a tie
    if print_game:
        game.print_board_nums()
    
    letter = 'X' #starting letter
    while game.empty_squares():
        #get the next move from appropriate player
        if letter == 'O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)
        
        if game.make_move(square, letter):
            if print_game:
                print(letter + f' makes a move to square {square}. ')
                game.print_board()
                print('')
            
            if game.current_winner:
                if print_game:
                    print(letter + ' wins! ')
                return letter
            
            #after we made our move, we need to alternate letters
            if letter == 'X':
                letter = 'O'
            else:
                letter = 'X'
                
    if print_game:
        print('It\'s a tie! ')

if __name__ == '__main__':
    x_player = HumanPlayer('X')
    o_player = RandomComputerPlayer('O')
    t = TicTacToe()
    play(t, x_player, o_player, print_game=True)
    