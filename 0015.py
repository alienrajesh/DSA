
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


def three3Sum(nums: list[int]) -> list[list[int]]:
    
    res = [ ]
    
    nums.sort()
    
    for i , a in enumerate(nums):
        
        if i > 0 and a == nums[i-1]:
            continue
        
        l , r = i+1 , len(nums) - 1
        
        while l < r :
            threesum = a + nums[l] + nums[r]
            
            if threesum > 0 :
                r-=1
            elif threesum < 0:
                l+=1
            else:
                res.append([a, nums[l] , nums[r]]) 

                l+=1
                r-=1
                while nums[l] == nums[l-1] and l < r:
                    l +=1
        
    return res            
  
  
print(three3Sum(nums))      
    
    