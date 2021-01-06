import numpy as np
import random


class Board:
    def __init__(self, difficulty):
        self.board = [[0 for c in range(9)] for cc in range(9)]
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

    def boardSolver(self, row, col):
        # TODO: recursion for solver
        if ((col == len(self.board)-1) and (row == len(self.board)-1)): # end of board (col == 8, row == 8) 
            print("end of board")
            return True
        elif (col == len(self.board)-1): # end of row (col = 8) 
            return self.boardSolver(row+1, 0)
        elif (self.board[row][col] != 0): # non-empty cell
            return self.boardSolver(row, col+1)   
        else: #empty cell
            # attemptInsert()
            return self.boardSolver(row, col+1)


    def printBoard(self):
        [print(self.board[c]) for c in range(len(self.board))]

if __name__ == "__main__":

    # TODO: difficulty affects how many cells removed at init
    # TODO: attach "holding" cells to board, maybe duplicate grid
    difficulty = ["Easy", "Moderate", "Hard"]
    #init board
    board = Board(difficulty[0])
    board.printBoard()
    board.boardSolver(0, 0)