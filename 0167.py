# Input: numbers = [2,7,11,15], target = 9
# Output: [1,2]
# Explanation: The sum of 2 and 7 is 9.
#             Therefore, index1 = 1, index2 = 2. We return [1, 2].


numbers = [0,0,0,0,3,3,3,4]
target = 0

def twoSum(numbers: list[int], target: int) -> list[int]:
    
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if i==j :
                continue
            elif numbers[i] + numbers[j] == target :
                return [i+1,j+1]
            
            

 



def twoSum2(numbers: list[int], target: int) -> list[int]:
    
    
    for i , n in enumerate(numbers):
        diff = target - n 
        if diff == n:
            return [i+1,i+2]
        if diff in numbers:
            return [i+1,(numbers.index(diff))+1]
            
            
            
        
        
print(twoSum2(numbers,target))  