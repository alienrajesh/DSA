# 2962. Count Subarrays Where Max Element Appears at Least K Times

# You are given an integer array nums and a positive integer k.
# Return the number of subarrays where the maximum element of nums appears at
# least k times in that subarray.
# A subarray is a contiguous sequence of elements within an array.
#
#
#
# Example 1:
# Input: nums = [1,3,2,3,3], k = 2
# Output: 6
# Explanation: The subarrays that contain the element 3 at least 2 times are:
# [1,3,2,3], [1,3,2,3,3], [3,2,3], [3,2,3,3], [2,3,3] and [3,3].
#
# Example 2:
# Input: nums = [1,4,2,1], k = 3
# Output: 0
# Explanation: No subarray contains the element 4 at least 3 times.
#
#
# Constraints:
# 1 <= nums.length <= 105
# 1 <= nums[i] <= 106
# 1 <= k <= 105


def countSubarrays(nums: list[int], k: int) -> int:
    max_num, max_count = max(nums), 0
    l = 0
    res = 0
    for r in range(len(nums)):

        if nums[r] == max_num:
            max_count += 1

        while max_count > k or (l <= r and max_count == k and nums[l] != max_num):
            if nums[l] == max_num:
                max_count -= 1
            l += 1

        if max_count == k:
            res += l + 1

    return res
