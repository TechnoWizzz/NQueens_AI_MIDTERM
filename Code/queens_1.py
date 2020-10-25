import numpy as np
import random
from copy import deepcopy
           
class nqueens:
    def __init__(self, start_x = random.randint(0,7), start_y = random.randint(0,7)):
        self.size = 8
        self.solved = False
        print(f'Board created with starting point: {start_x},{start_y}')
        self.board = np.zeros((self.size,self.size))
        self.col_order = list(range(start_x, self.size))
        self.col_order += list(range(0,start_x))
        self.row_order = list(range(start_y, self.size))
        self.row_order += list(range(0,start_y))
        self.completed = False
        self.curr_col = 0
        self.tries = 0
        
    def check_placement(self,x,y):
        #Check column
        if 1 in self.board[x]:
            return False
        #Check row
        elif 1 in self.board[:, y]:
            return False
        #Check forward diagonal
        elif 1 in np.diag(self.board, y):
            return False
        #Check backwards diagonal
        elif 1 in np.diag(np.fliplr(self.board), 7-y):
            return False
        else:
            return True
        
    def backtrack_search(self):
        self.board[self.row_order[0], self.col_order[0]] = 1
        self.curr_col+=1
        if(self.backtrack_recursion(self.col_order[self.curr_col])):
            print(f'Solution has been found as follows!:\n\n')
            for i in range(0,8):
                print(f'{self.board[i]}')
        else:
            print("A solution could not be found with the given starting position")
        
    def backtrack_recursion(self, col):
        for val in self.row_order:
            self.tries+=1
            if self.check_placement(col, val):
                self.curr_col+=1
                self.board[val][col] = 1
                if self.curr_col == self.size:
                    return True
                if (self.backtrack_recursion(self.col_order[self.curr_col+1])):
                    return True
                self.curr_col-=1
                self.board[val][col] = 0
        return False
            
# def main():
    # N_Queens_()
    
# if __name__ == "__main":
    # main()