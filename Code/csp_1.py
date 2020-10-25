import numpy as np
import random
import string
from copy import deepcopy

class csp:
    def __init__(self, col=random.randint(0,7), row=random.randint(0,7)):
        self.board = np.zeros((8,8))
        self.board[row][col] = 1
        self.start= [col,row]
        self.placed = 1
        print(self.start)
        
    def place_queen(self, val, loc):
        self.board[loc[0]][loc[1]] = val
        
    def check_placement(self, col, row):
        #Check column
        if 1 in self.board[row]:
            return False
        #Check row
        elif 1 in self.board[:, col]:
            return False
        #Check forward diagonal
        elif 1 in np.diag(self.board, col-row):
            return False
        #Check backwards diagonal
        elif 1 in np.diag(np.fliplr(self.board), (7-(row+col))):
            return False
        else:
            return True
            
    def backtrack(self):
        if(self.backtack_rec(self.start[0]+1)):
            print(f'Solution has been found as follows:\n{self.board}\n')
        else:
            print(f'A solution could not be found with the given starting queen placement')
    
    def backtack_rec(self, col):
        if self.placed == 8:
            return True
        if(col == 8):
            col = 0
        for val in range(8):
            if self.check_placement(col, val):
                self.placed+=1
                self.board[val][col] = 1
                if self.backtack_rec(col+1):
                    return True
                self.board[val][col] = 0
                self.placed-=1
        return False
        
    def forward_checking(self):
        if(self.forward_rec(self.start[0]+1)):
            print(f"Solution has been found using forward checking as follow:\n{self.board}")
        else:
            print(f'A solution could not be found with the given starting queen placement:\n{self.start}')
            
    def forward_rec(self, col):
    #MODIFY - NEED TO KEEP TRACK OF DOMAINS OF EACH QUEEN POSSIBILITY AT ALL TIME. EX: QUEENS_DOMAINS[[0,1,2,3,4,5,6,7],[0,1,2,3,4,5,6,7],...]
    #REMOVE FROMQUEENS DOMAIN WHEN MAKING A PLACEMENT
        if self.placed == 8:
            return True
        if col ==8:
            col = 0
        possibleRows = []
        for val in range(0,8):
            if self.check_placement(col,val):
                possibleRows.append(val)
        for row in possibleRows:
            if self.check_placement(col, row): #REPLACE WITH CHECK_DOMAIN
                self.placed+=1
                self.board[row][col] = 1
                #MODIFY DOMAINS HERE AFTER PLACING A QUEEN
                if self.backtack_rec(col+1):
                    return True
                self.board[row][col] = 0
                self.placed-=1
        return False
        
        
        
        
        