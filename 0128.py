#longest consecutive sequence
# Input: nums = [100,4,200,1,3,2]
# Output: 4
# Explanation: The longest consecutive elements sequence is
#              [1, 2, 3, 4]. Therefore its length is 4.

# [1,2,3,4,100,200]
# [ 1, 3 , 4, 5, 6, 100, 200]

nums =  [ ]

def longestConsecutive(nums: list[int]) -> int:
    
    nums.sort()
    print(nums)
    max = 0 
    counter = 0
    for i in range(len(nums)-1):
        if nums[i+1] - nums[i] == 1 :
            counter +=1
        else:
           counter = 0
            
        if max < counter :
            max = counter
        
                  
    return max + 1
           

def  longestConsecutive(nums: list[int]) -> int:
    numSet = set(nums)
    
    longest = 0
    
    for n in numSet: 
        if (n-1) not in numSet:
            length = 0
            while n+length in numSet:
               length += 1
            longest = max(length, longest)
    return longest
      
        
        
    
    
    
    
    
print(longestConsecutive(nums))    