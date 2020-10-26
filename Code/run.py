#Import csp object and respective functions from the respective py file
from csp_1 import csp


#Create NQueens csp object
test = csp(0,0)
#Run backtracking search on nqueens csp
test.backtrack()
#Create NQueens csp object with randomized initial queen placement
test = csp(0,0)
#Run forward checking search on randomized NQueens csp object
test.forward_checking()