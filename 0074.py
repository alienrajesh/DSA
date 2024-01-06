# 0074.py Search in a 2D matrix


# EXAMPLE 1:

# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
# Output: true


# EXAMPLE 2:


# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
# Output: false

matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]

target = 60

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

    return "number not found"

    
print(searchMatrix(matrix,target))