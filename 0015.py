
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
    
    res = [ ]
    
    nums.sort()
    
    for i , a in enumerate(nums):
        
        if i > 0 and a == nums[i-1]:
            continue
        
        l , r = i+1 , len(nums) - 1
        
        while l < r :
            sum = a + nums[l] + nums[r]
            
            if sum > 0 :
                r-=1
            elif sum < 0:
                l+=1
            else:
                res.append([a, nums[l] , nums[r]]) 

                l+=1
                r-=1
                while nums[l] == nums[l-1] and l < r:
                    l +=1
        
    return res            
  
  
# print(threeSum(nums))      
    


def threesum(nums: list[int]) -> list[list[int]]:
     
    res = [] 
    
    nums.sort() 
    
    for i , a in enumerate(nums):
        # skip positive integers
        if a > 0 :
            break
        
        
        if i > 0 and a == nums[i-1]:
            continue
        
        l , r = i +1 , len(nums) -1
        
        while l < r :
            
            sum = a + nums[l] + nums[r] 
            
            if  sum < 0 :
                l+=1
            elif sum>0 :
                r-=1
            else:
                res.append([a, nums[l] , nums[r]])
                l+=1
                r-=1
                
                while nums[l] == nums[l-1] and l<r :
                    l+=1
                    
    return res

# print(threesum(nums))


# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]


            
def threesum2(nums: list[int]) -> list[list[int]]:
      
    res = []
    nums.sort()
    
    
    for  i , a in enumerate(nums):
        #skips +ve int
        if a > 0 :
            break 
        
        #checks for same element
        if i > 0 and a == nums[i-1]:
            continue
        
        l , r = i +1 , len(nums) -1       # [-1, 0, 1, 2, -1, -4]
                                          #   i  l             r
        while l < r :
            
            sum = a + nums[l] + nums[r]
            
            if sum > 0 :
                r-=1
            elif sum < 0:
                l +=1
            else :
                res.append([a,nums[l] , nums[r]])
                
                l += 1
                r -= 1

                while l < r and nums[l] == nums[l-1]:
                    l+=1
    print(res)

            
threesum2(nums )            
            
            
            
            
def threesum3(nums:list[int]) -> list[list[int]]:
    
    res = []
    nums.sort()

    
    
    for i , a in enumerate(nums) :
        
        if a > 0 :
            break
        
        if i > 0 and a == nums[i-1] :
            continue
        
        l , r = i + 1 , len(nums)-1
        
        while l < r : 
        
            sum = a + nums[l] + nums[r]

            if sum > 0 :
                r-=1
            elif sum < 0 :
                l+=1

            else : 
                res.append([i,nums[l],nums[r]])
                
                l+=1
                r-=1
                
                while l < r and nums[l] == nums[l-r] : 
                    l+=1
    return res
    
print(threesum3(nums) )   