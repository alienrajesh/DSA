# 0074.py Search in a 2D matrix


# EXAMPLE 1:

# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
# Output: true


# EXAMPLE 2:


# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
# Output: false

matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]

target = 4

def searchMatrix(matrix: list[list[int]], target: int) -> bool:
    
    new = []
    
    # unpacking the matrix
    for r in matrix:
        new.extend(r)
    
    # binary search
    l , h = 0 , len(new)
    
    while l <= h :
        mid = (l+h) // 2
        number = new[mid]
        
        if number > target:
            h = mid -1
        elif number < target :
            l = mid +1
        else:
            return number

    return "Number Not Found"
    
# NEETCODE solution 
# time  - O(log(m*n))
# space -

def searchMatrix2( nums:list[list[int]] , target :int):
    
    rows , cols = len(matrix) , len(matrix[0])
    
    top , bottom = 0 , rows -1 
    
    while top <= bottom :
        row = (top+bottom) // 2
        
        if target > matrix[row][-1] :
            top = row + 1 
        elif target < matrix[row][0]:
            bottom = row - 1 
        else:
            break 
        
    if not (top <= bottom):
        return False

    l , r = 0 , cols -1
    
    while l <= r :
        mid = (l+r) // 2 
        
        if target > matrix[row][mid] :
            l = mid + 1 
        elif target < matrix[row][mid]:
            r = mid -1
        else:
            return True

    return False
            
           
    
print(searchMatrix2(matrix,target))




















