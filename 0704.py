# 0704.py Binary Search



# Example 1:

# Input: nums = [-1,0,3,5,9,12], target = 9
# Output: 4
# Explanation: 9 exists in nums and its index is 4


# Example 2:

# Input: nums = [-1,0,3,5,9,12], target = 2
# Output: -1
# Explanation: 2 does not exist in nums so return -1

nums = [-1,0,3,5,9,12]
target = 12

def search(nums: list[int] , target: int) -> int:
    
    l , h = 0 , len(nums)
    # print(f"h - {h}")
    
    while l <= h :
        mid = (l+h) // 2
        # print(mid)
        number = nums[mid]
        
        if number == target:
            return number
        
        if number < target :
            l = mid + 1
        
        elif number > target:
            h = mid -1
    
    return "Number not present" 


print(search(nums,target))   