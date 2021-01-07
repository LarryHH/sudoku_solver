import numpy as np
import random

class Board:
    def __init__(self, difficulty):
        self.board = np.array([[0 for c in range(9)] for cc in range(9)])
        self.difficulty = difficulty
        self.initBoardDiagonal(0)

    def initBoardDiagonal(self, start):

        rowConstant = start                  
        colConstant = rowConstant + 2          

        col = colConstant                       
        row = rowConstant                       

        numbers = random.sample(range(1, 10), 9)

        for c in range(len(numbers)):
            if((col >= rowConstant)):
                self.board[row][col] = numbers[c]
                col -= 1
            if((col < rowConstant)):
                row += 1
                col = colConstant
        if(start < 6):
            self.initBoardDiagonal(start+3)


    def attemptInsert(self, r, c, num):
        r1, r2, c1, c2 = self.checkTridrant(r, c)
        if (num in self.board[r,:]) | (num in self.board[:,c]):
            return False
        elif (num in self.board[r1:r2,c1:c2]):
            return False
        else:
            self.board[r][c] = num
            return True


    def boardSolver(self, row, col):
        print(row, col)
        if ((col == len(self.board)-1) and (row == len(self.board)-1)): # end of board (col == 8, row == 8) 
            print("end of board")
            return True
        elif (col > len(self.board)-1): # end of row (col = 8) 
            return self.boardSolver(row+1, 0)
        elif (self.board[row][col] != 0): # non-empty cell
            return self.boardSolver(row, col+1)   
        else: #empty cell
            # TODO: this recursion doesn't work, need to figure this one out
            for num in list(range(1,10)):
                if (self.attemptInsert(row, col, num)):
                    return self.boardSolver(row, col+1)
                else:
                    continue

    def printBoard(self):
        [print(self.board[c]) for c in range(len(self.board))]

    def checkTridrant(self, row, col):
        row_tridrant = row/3
        col_tridrant = col/3
        if row_tridrant < 1 and col_tridrant < 1:
            return (0, 3, 0, 3)
        if row_tridrant < 1 and col_tridrant < 2:
            return (0, 3, 3, 6)
        if row_tridrant < 1 and col_tridrant < 3:
            return (0, 3, 6, 9)
        if row_tridrant < 2 and col_tridrant < 1:
            return (3, 6, 0, 3)
        if row_tridrant < 2 and col_tridrant < 2:
            return (3, 6, 3, 6)
        if row_tridrant < 2 and col_tridrant < 3:
            return (3, 6, 6, 9)                        
        if row_tridrant < 3 and col_tridrant < 1:
            return (6, 9, 0, 3)
        if row_tridrant < 3 and col_tridrant < 2:
            return (6, 9, 3, 6)
        if row_tridrant < 3 and col_tridrant < 3:
            return (6, 9, 6, 9)

if __name__ == "__main__":
    # TODO: recursion for solver
    # TODO: difficulty affects how many cells removed at init
    # TODO: attach "holding" cells to board, maybe duplicate grid

    difficulty = ["Easy", "Moderate", "Hard"]
    #init board

    board = Board(difficulty[0])
    board.boardSolver(0, 0)
    board.printBoard()