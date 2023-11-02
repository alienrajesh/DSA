

#Input: nums = [1,2,3,4]
#Output: [24,12,8,6]

nums = [1,2,3,4]

#division method is not allowed on leetcode
def productExceptSelf(nums: list[int]) -> list[int]:
    res = []
    multiply = 1
    for i in range(0,len(nums)):
        multiply = multiply*nums[i]
    
    for i in nums:
        res.append(multiply//i)    
    print(res)

#the above function will not work on the input given below        
# Input: nums = [-1,1,0,-3,3]
# Output: [0,0,9,0,0]
       
# productExceptSelf(nums)        

#Input: nums = [1,2,3,4]
#Output: [24,12,8,6]

# time  - O(n^2)
# space - O(n)
def productExceptSelf1(nums: list[int]) -> list[int]:
    res = []
    for i in range(0,len(nums)):
        temp = 1
        for j in range(0,len(nums)):
            if i == j :
                continue
            else:
                temp *= nums[j]
        res.append(temp)
    print(res)

# productExceptSelf1(nums)



#neetcode solution
# time - O(n)
# space - O(1) acc to question the output array does not require space

def productExceptSelf2(nums: list[int]) -> list[int]:
    res = [1] * len(nums)
    
    prefix = 1
    for i in range(len(nums)):
        res[i] = prefix
        prefix *= nums[i]
    
    postfix = 1
    for i in range(len(nums)-1, -1 , -1):
        res[i] = postfix
        postfix *= nums[i]
        
    print(res)      
 
productExceptSelf2(nums)   