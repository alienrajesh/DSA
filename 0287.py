# Given an array of integers nums containing n + 1 integers where each
# integer is in the range [1, n] inclusive.

# There is only one repeated number in nums, return this repeated number.

# You must solve the problem without modifying the array nums
# and uses only constant extra space.


# Example 1:
#
# Input: nums = [1,3,4,2,2]
# Output: 2


# Example 2:
#
# Input: nums = [3,1,3,4,2]
# Output: 3

def findDuplicate( nums: [int]) -> int:
    slow = fast = 0

    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]

        if slow == fast:
            break

    slow2 = 0
    while True:
        slow = nums[slow]
        slow2 = nums[slow2]

        if slow == slow2 :
            return slow

def test_findDuplicate():
    # Test case 1: Single duplicate element
    nums1 = [1, 3, 4, 2, 2]
    assert findDuplicate(nums1) == 2

    
    # Test case 2: Multiple duplicate elements
    nums2 = [3, 1, 3, 4, 2]
    assert findDuplicate(nums2) == 3

    # Test case 3: Large array with multiple duplicates
    nums5 = [1, 2, 3, 4, 5, 5, 6, 7, 8, 9, 10, 5]
    assert findDuplicate(nums5) == 5

    print("All test cases passed!")
    
test_findDuplicate()
