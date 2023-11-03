class TicTacToe:
    def __init__(self):
        self.board = [' 'for _ in range(9)]#A list to create board
        self.currentWinner = None
    
    def printBoard(self):
        for row in [self.board[i*3:(i+1*3)] for i in range(3)]:
            print("| " + " | ".join(row) + " |")
    

    @staticmethod
    def printBoardNums():
        numberBoard = [[str(i)for i in range(j*3,(j+1)*3)]for j in range(3)]
        for row in numberBoard:
            print("| " + " | ".join(row) + " |")
    def availableMoves(self):  
        moves = []
        for (i,  spot) in enumerate(self.board):
            if spot == ' ':
                moves.append(i)
        return moves
    def emptySquares(self):
        return ' ' in self.board
    def numEmptySquares(self):
        return len(self.availableMoves)
    def makeMove(self, square, letter):
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.currentWinner = letter
            return True
        return False
    def winner(self, square, letter):
        #winner if 3 in row or column or diag
        rowIndex = square//3
        row = self.board[rowIndex*3:(rowIndex+1)*3]
        if all(spot==letter for spot in row):
            return True
        colIndex = square%3
        column = [self.board[colIndex + i*3] for i in range(3)]
        if all(spot==letter for spot in column):
            return True
        if square%2==0:
            diagonal1 = [self.board[i]for i in [0, 4, 8]]
            if all(spot==letter for spot in diagonal1):
                return True
           
            diagonal2 = [self.board[i]for i in [2, 4, 6]]
            if all(spot==letter for spot in diagonal2):
                return True
        return False
            
def game(game,xPlayer, oPlayer, printGame = True):
    if printGame:
        game.printBoardNums()
    letter = 'X'
    while game.emptySquares():
        if letter=='O':
            square = oPlayer.getMove(game)
        else:
            square = xPlayer.getMove(game)
        if game.makeMove(square,letter):
            if printGame:
                print(letter + f'makes a move to square{square}')
                game.printBoard()
                print(" ")
            if game.currentWinner:
                if printGame:
                    print(letter + 'wins!')
                return letter
            
            letter='O' if letter =='X' else 'X'

    if printGame:
        print("It's a tie")
