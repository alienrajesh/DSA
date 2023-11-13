
# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
# Explanation: 
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
# The distinct triplets are [-1,0,1] and [-1,-1,2].
# Notice that the order of the output and the order of the triplets does not matter.

# nums[i] + nums[j] == - nums[k] 

nums = [-1,0,1,2,-1,-4]


def threeSum(nums: list[int]) -> list[list[int]]:
    l , r = 0 , len(nums) - 1
    
    
    res = [ ]
    while l < r:
        m = (l+r) //2
        
        if nums[l] + nums[m] + nums[r] == 0:
            res.append([nums[l], nums[m] , nums[r]]) 
            
            
        while  nums[l] + nums[m] + nums[r] != 0 :
            l+=1
        
        
    return res    
        
    
  
print(threeSum(nums))      
    
    