import collections


def row_coulum():   
        for i in range(0,9):
            hashMapC, hashMapR = {} , {}
            for j in range(0,9):
            #column check     
                if board[j][i] == ".":
                    continue
                elif hashMapC.get(board[j][i],False) == True :
                    return False
                else :
                    hashMapC[board[j][i]] = True
            #Row check        
                if board[i][j] == ".":
                    continue
                elif hashMapR.get(board[i][j],False) == True :
                    return False
                else:
                    hashMapR[board[i][j]] = True
        return True   

#Valid sudoku
# Input: board = 
# [["5","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]
# Output: true


# def isValidSudoku(board: list[list[str]]) -> bool:
    
#     for i in range(0,9,2):
        
        
                  
                  
board = [
     ["5","3",".",".","7",".",".",".","."],
     ["6",".",".","1","9","5",".",".","."],
     [".","9","8",".",".",".",".","6","."],
     ["8",".",".",".","6",".",".",".","3"],
     ["4",".",".","8",".","3",".",".","1"],
     ["7",".",".",".","2",".",".",".","6"],
     [".","6",".",".",".",".","2","8","."],
     [".",".",".","4","1","9",".",".","5"],
     [".",".",".",".","8",".",".","7","9"],
]                  

               
                  
# print(isValidSudoku(board)) 



#neetcode solution

def isValidSudoku2(board: list[list[str]]) -> bool:
    rows = collections.defaultdict(set)
    columns = collections.defaultdict(set)
    squares = collections.defaultdict(set)
    
    for r in range(9):
        for c in range(9):
            if board[r][c] == "." :
                continue
            
            if (   board[r][c] in rows[r] or
                board[r][c] in columns[c] or 
                board[r][c] in squares[(r//3 , c//3)]):
             
                 return False
            
            rows[r].add(board[r][c])
            columns[c].add(board[r][c])
            squares[(r//3,c//3)].add(board[r][c])
            print(squares)
    return True        







def isValidSudoku(board):
        rows = collections.defaultdict(set)
        columns = collections.defaultdict(set)
        squares =  collections.defaultdict(set)
        
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                 
                if (board[r][c] in rows[r] or
                board[r][c] in columns[c] or
                board[r][c] in squares[(r//3,c//3)]
                ):   
                    return False
                
                rows[r].add(board[r][c])
                columns[c].add(board[r][c])
                squares[(r//3,c//3)].add(board[r][c])
                
      
        return True
    
print(isValidSudoku(board))    

