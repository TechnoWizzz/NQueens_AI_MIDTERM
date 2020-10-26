import numpy as np
import random

#CSP object used to instantiate nqueens setup and includes the various types of searches
#that you would run on the nqueens initial queen placement
class csp:
    def __init__(self, col=random.randint(0,7), row=random.randint(0,7)):
        self.board = np.zeros((8,8))
        self.board[row][col] = 1
        self.start= [col,row]
        self.queen_domains = [[0,1,2,3,4,5,6,7],[0,1,2,3,4,5,6,7],[0,1,2,3,4,5,6,7],[0,1,2,3,4,5,6,7],[0,1,2,3,4,5,6,7],[0,1,2,3,4,5,6,7],[0,1,2,3,4,5,6,7],[0,1,2,3,4,5,6,7]]
        self.placed = 1
        print(f'{self.start}, formatted as [col,row] starting from 0')
        
    #Modifies the object's 'board' variable and adds a marker designating a queen has been placed in that location
    def place_queen(self, val, loc):
        self.board[loc[0]][loc[1]] = val
    
    #Checks a possible queen placement so that no queen already on the board is contested by it    
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
            
    #Initial function call to begin backchecking search and print results when finished
    def backtrack(self):
        if(self.backtack_rec(self.start[0]+1)):
            print(f'Solution has been found as follows:\n{self.board}\n')
        else:
            print(f'A solution could not be found with the given starting queen placement')
    
    #Recursive function that will iterate through the queen placements until a solution is found or found to be impossiblle with
    #the given starting queen placement
    def backtack_rec(self, col):
        #Returns true when all queens have been placed
        if self.placed == 8:
            return True
        #Compensates for when starting position is not the first column
        if(col == 8):
            col = 0
        #Iterate through each row of the column that is being filled
        for val in range(8):
            #Check if col,row placement is possible with the current board
            if self.check_placement(col, val):
                #Fills place if placement passes check
                self.placed+=1
                self.board[val][col] = 1
                #Continue onto the next column recursively
                if self.backtack_rec(col+1):
                    return True
                #Removes placement because if statement above returns false, the placement is a dead end in the search
                self.board[val][col] = 0
                self.placed-=1
        #If all placements are tried and not possible, returns false signaling that the previous column is not the correct placement and backtracks
        return False
    #Initial function call to begin forward checking search and print results when finished    
    def forward_checking(self):
        if(self.forward_rec(self.start[0]+1)):
            print(f"Solution has been found using forward checking as follow:\n{self.board}")
        else:
            print(f'A solution could not be found with the given starting queen placement:\n{self.start}')
    
    #Recursive function that will iterate through the queen placements until a solution is found or found to be impossiblle with
    #the given starting queen placement
    def forward_rec(self, col):
        #Returns true when all queens have been placed
        if self.placed == 8:
            return True
        #Compensates for when starting position is not the first column
        if col ==8:
            col = 0
        #Forward check possible placements for the current column
        for val in self.queen_domains[col]:
            if not self.check_placement(col,val):
                self.queen_domains[col][val] = -9
        #Evaluate the next column using possible values from the modified domain of the current column
        for row in self.queen_domains[col]:
            if row != -9:
                self.placed+=1
                self.board[row][col] = 1
                if self.forward_rec(col+1):
                    return True
                self.board[row][col] = 0
                self.placed-=1
        self.queen_domains[col] = [0,1,2,3,4,5,6,7]
        return False
        
    #def arc_consistency(self)
        
        