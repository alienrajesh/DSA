# 0033.py Search in Rotated Sorted Array

# Example 1:

# Input: nums = [4,5,6,7,0,1,2], target = 0
# Output: 4


# Example 2:

# Input: nums = [4,5,6,7,0,1,2], target = 3
# Output: -1


# Example 3:

# Input: nums = [1], target = 0
# Output: -1

# TestCase - nums = [5,1,2,3,4] , target = 1 , output = 1


# Brute force 
# Time - O(N)
# Space - O(1)

nums =[5,1,2,3,4]
target = 1

def search(nums:list[int],target) -> int:
    
    for r in range(len(nums)):
        if nums[r] == target:
            return r 
    return -1

def search2(nums: list[int], target: int) -> int:
    
    l , r = 0 , len(nums)-1
    
    while l<=r :
        m = (l+r) // 2 
        if nums[m] == target :
            return m 
        
        # left sorted portion 
        if nums[l] <= nums[m] :
            if target > nums[m] or target < nums[l]:
                l = m +1
            else:
                r = m -1
        # right sorted portion
        else:
            if target < nums[m] or target > nums[r]:
                r = m - 1 
            else: 
                l = m + 1
        
    return -1


print(search2(nums,target))