# 713. Subarray Product Less Than

# Problem Statement
# Given an array of integers nums and an integer k, return the number of
# contiguous subarrays where the product of all the elements in the subarray is
# strictly less than k.
#
#
# Example 1:
# Input: nums = [10,5,2,6], k = 100
# Output: 8
# Explanation: The 8 subarrays that have product less than 100 are:
# [10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6]
# Note that [10, 5, 2] is not included as the product of 100 is not strictly less than k.
#
# Example 2:
# Input: nums = [1,2,3], k = 0
# Output: 0
#
# Constraints:
# 1 <= nums.length <= 3 * 104
# 1 <= nums[i] <= 1000
# 0 <= k <= 106


# Notes :
# Method 1 : sliding Window
# Method 2 : binary search with Logarithm
# Solution
def numSubarrayProductLessThanK(self, nums: list[int], k: int) -> int:
    res = 0
    l = 0
    product = 1

    if k == 0:
        return 0

    for r in range(len(nums)):
        product *= nums[r]
        while l <= r and product >= k:
            product = product // nums[l]
            l += 1

        res += r - l + 1

    return res


# Approach 2: Using Binary Search
# Intuition
# Logarithms have the property that the sum of logarithms is "approximately
# equivalent" to the logarithm of the product. This property allows us to convert
# the product of elements in a subarray to the sum of the logarithms of those
# elements.
#
# The motivation for this is that the product of some arbitrary subarray may be
# way too large (potentially 1000500001000^{50000}1000 50000).
#
# Integer overflow occurs when the result of an arithmetic operation exceeds the
# maximum value represented by the data type. This can happen when computing the
# product of elements in a large subarray, as the result can quickly surpass the
# integer's capacity, leading to incorrect values due to overflow.
#
# To mitigate this, we can convert the product operation into a summation of
# logarithms. Logarithms allow the representation of large values within a
# manageable range, minimizing the risk of overflow while maintaining accuracy.
#
# The first step is to transform the problem from finding products to finding
# sums. This is done by taking the natural logarithm (log) of each element in the
# array.
#
# Then a prefix sum array (logsPrefixSum) is calculated, where each element is
# the sum of the logarithms of all elements up to that point in the original
# array. This will allow us to quickly determine if a subarray's sum of
# logarithms is less than a certain value. Because the prefix sum is a
# monotonically increasing array, we can use binary search to find valid
# subarrays.
#
# For each element in the array, a binary search is performed to find the number
# of subarrays starting from that element whose sum of logarithms is less
# than the sum of the logarithms of the current element and log(K). This
# is done by comparing the midpoint of the search space with the sum of the
# logarithms of the current element and log(K). If the midpoint is too
# high, the search space is narrowed to the left; otherwise, it's narrowed to
# the right. The number of subarrays found is added to the total count.
#
# Logarithmic comparisons have an issue due to the finite precision in
# floating-point number representation. That is, logarithmic functions can lead
# to very small differences between numbers that should be equal, especially
# when dealing with large or small values.
#
# The product rule is log⁡(a⋅b)==log⁡(a)+log⁡(b)\log(a \cdot b)
# == \log(a) + \log(b)log(a⋅b)==log(a)+log(b), but these expressions may not be
# evaluated as equivalent due to floating-point representation in the computer.
# It may be log⁡(a⋅b)>log⁡(a)+log⁡(b)\log(a \cdot b) > \log(a) +
# \log(b)log(a⋅b)>log(a)+log(b) or
# log⁡(a⋅b)<log⁡(a)+log⁡(b)\log(a \cdot b) < \log(a) +
# \log(b)log(a⋅b)<log(a)+log(b) . When we transform x to log(x), we introduce a
# possible bug.
#
# To prevent this from causing an issue, we subtract 1e-9 (which is a very
# small number, 0.000000001), in the comparison condition as a precautionary
# measure to handle potential precision issues that might arise due to the
# nature of logarithmic values. This helps mitigate the effect of these
# precision errors by providing a small buffer or tolerance in the comparison.
# Even though logarithmic values tend to spread out differences across a wider
# range, there can still be cases where very close values need to be
# distinguished, and small discrepancies can occur due to finite precision.
#
# In essence, it ensures that if logsPrefixSum[mid] is very close to
# logsPrefixSum[i] + logK, the former will still be considered less than the
# latter rather than failing the condition due to slight numerical
# discrepancies.
#
# This kind of adjustment is common in numerical math computations where
# precision matters, especially in conditional algorithms where small
# discrepancies could lead to incorrect results or sometimes infinite loops.
#
# Algorithm
# Check if k (target product) is 0. If true, return 0 (no subarrays possible).
# Calculate the logarithm of k and store it in logK.
# Create a vector logsPrefixSum of size nums.size() + 1 to store the prefix sum
# of logarithms of elements in nums.
# Calculate the prefix sum by iterating over nums and adding the logarithm of
# each element to the previous prefix sum. This creates a running sum of
# logarithms for efficient product calculation later.
# Initialize totalCount to 0, which will keep track of the total number of
# subarrays with a product less than k. Iterate through logsPrefixSum using a
# loop with index currIdx. This loop considers each element (nums[currIdx]) as
# the starting point of a potential subarray. Inside the loop, initialize two
# variables, low and high, to currIdx + 1 and m (nums.size() + 1),
# respectively. Enter a binary search loop to find the first element in
# logsPrefixSum where the subarray product (based on logarithms) exceeds k.
# Calculate the middle index mid between low and high. Compare the prefix sum
# at mid with the target prefix sum (logsPrefixSum[currIdx] + logK). Here, a
# small tolerance (-1e-9) is used to handle floating-point precision issues. If
# the prefix sum at mid is less than the target, it means the subarray product
# ending at mid might still be less than k. Move low to mid + 1 to search in
# the right half of the remaining subarray. Otherwise, the subarray product
# ending at mid or elements beyond mid might exceed k. Move high to mid to
# continue searching in the left half for the first exceeding element. After
# the binary search loop, the low index points to the first element in
# logsPrefixSum where the subarray product (based on logarithms) exceeds k.
# Increment totalCount by the number of elements between currIdx (inclusive)
# and low (exclusive). This represents the number of valid subarrays ending at
# currIdx with a product less than k. Finally, return totalCount.

# Implementation
# class Solution:
#     def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
#         if k == 0: return 0
#         logK = math.log(k)
#
#         # Calculate prefix sum of logarithms of elements
#         logs_prefix_sum = [0]
#         for num in nums:
#             logs_prefix_sum.append(logs_prefix_sum[-1] + math.log(num))
#
#         total_count = 0
#         # Calculate subarray count with product less than k
#         for i, log_num in enumerate(logs_prefix_sum):
#             j = bisect.bisect(logs_prefix_sum, log_num + logK - 1e-9, i+1)
#             total_count += j - i - 1
#         return total_count
