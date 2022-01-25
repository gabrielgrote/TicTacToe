class Tictactoe:
    def __init__(self):
        self.board = ['-','-','-',
                      '-','-','-',
                      '-','-','-',]
        self.turn = True
        self.occupiedPos = []
        self.gameStatus = True
    
    def printBoard(self):
        print(self.board[6:])
        print(self.board[3:6])
        print(self.board[:3])
    
    def changeTurns(self):
        if self.turn == True:
            self.turn = False
        else:
            self.turn = True
    
    def play(self):
        move = input('select from 1 to 9: ')
        return move
    
    def checkMove(self, move):
        if move.isdigit() and int(move) not in self.occupiedPos and int(move) in range(1,10):
            if self.turn:
                self.board[int(move)-1] = 'x'
                self.occupiedPos.append(int(move))

            if not self.turn:
                self.board[int(move)-1] = 'o'
                self.occupiedPos.append(int(move))
        else:
            return
    
    def verifyWinner(self):
        # checks X is winner
        # horizontal
        if self.board[:3] == ['x', 'x', 'x']:
            self.printBoard()
            print('X is the winner')
            self.gameStatus = False
        if self.board[3:6] == ['x', 'x', 'x']:
            self.printBoard()
            print('X is the winner')
            self.gameStatus = False
        if self.board[6:] == ['x', 'x', 'x']:
            self.printBoard()
            print('X is the winner')
            self.gameStatus = False
        # diagonal
        if self.board[0] == self.board[4] == self.board[7] == 'x':
            self.printBoard()
            print('X is the winner')
            self.gameStatus = False
        if self.board[2] == self.board[4] == self.board[6] == 'x':
            self.printBoard()
            print('X is the winner')
            self.gameStatus = False
        # vertical
        if self.board[0] == self.board[3] == self.board[6] =='x':
            self.printBoard()
            print('X is the winner')
            self.gameStatus = False
        if self.board[1] == self.board[4] == self.board[7] =='x':
            self.printBoard()
            print('X is the winner')
            self.gameStatus = False
        if self.board[2] == self.board[5] == self.board[8] =='x':
            self.printBoard()
            print('X is the winner')
            self.gameStatus = False
        
        # checks if O is winner
        # horizontal
        if self.board[:3] == ['o', 'o', 'o']:
            self.printBoard()
            print('O is the winner')
            self.gameStatus = False
        if self.board[3:6] == ['o', 'o', 'o']:
            self.printBoard()
            print('O is the winner')
            self.gameStatus = False
        if self.board[6:] == ['o', 'o', 'o']:
            self.printBoard()
            print('O is the winner')
            self.gameStatus = False
        # diagonal
        if self.board[0] == self.board[4] == self.board[7] == 'o':
            self.printBoard()
            print('O is the winner')
            self.gameStatus = False
        if self.board[2] == self.board[4] == self.board[6] == 'o':
            self.printBoard()
            print('O is the winner')
            self.gameStatus = False
        # vertical
        if self.board[0] == self.board[3] == self.board[6] =='o':
            self.printBoard()
            print('O is the winner')
            self.gameStatus = False
        if self.board[1] == self.board[4] == self.board[7] =='o':
            self.printBoard()
            print('O is the winner')
            self.gameStatus = False
        if self.board[2] == self.board[5] == self.board[8] =='o':
            self.printBoard()
            print('O is the winner')
            self.gameStatus = False
        
        
ttt = Tictactoe()

while ttt.gameStatus == True:
    ttt.printBoard()
    ttt.checkMove(ttt.play())
    ttt.changeTurns()
    ttt.verifyWinner()
