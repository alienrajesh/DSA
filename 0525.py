# 0525. Contiguous Array
# Given a binary array nums, return the maximum length of a contiguous subarray
# with an equal number of 0 and 1.
#
# Example 1:
#
# Input: nums = [0,1]
# Output: 2
# Explanation: [0, 1] is the longest contiguous subarray with an equal number of 0 and 1.
# Example 2:
#
# Input: nums = [0,1,0]
# Output: 2
# Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal
# number of 0 and 1.
#
# Constraints:
# 1 <= nums.length <= 105
# nums[i] is either 0 or 1.

# Solution
# Time - O(N) Space - O(N)
def findMaxLength(nums: list[int]) -> int:
    zero , one = 0,0
    res = 0

    diff_index = {} # count_ones - count_zeroes --> index 

    for i, n in enumerate(nums):
        if n == 0 :
            zero +=1
        else:
            one +=1 

        if (one-zero) not in diff_index:
            diff_index[one-zero] = i

        if one == zero:
            res = one + zero
        else:
            idx = diff_index[one-zero] 
            res = max(res,i-idx)
    return res

