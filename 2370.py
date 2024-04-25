# 2370. Longest Ideal Subsequence
#
# You are given a string s consisting of lowercase letters and an integer k. We
# call a string t ideal if the following conditions are satisfied:
# t is a subsequence of the string s.
# The absolute difference in the alphabet order of every two adjacent letters in
# t is less than or equal to k.
# Return the length of the longest ideal string.
# A subsequence is a string that can be derived from another string by deleting
# some or no characters without changing the order of the remaining characters.
# Note that the alphabet order is not cyclic. For example, the absolute
# difference in the alphabet order of 'a' and 'z' is 25, not 1.
#
#
#
# Example 1:
# Input: s = "acfgbd", k = 2
# Output: 4
# Explanation: The longest ideal string is "acbd". The length of this string is
# 4, so 4 is returned.
# Note that "acfgbd" is not ideal because 'c' and 'f' have a difference of 3 in
# alphabet order.
#
#
# Example 2:
# Input: s = "abcd", k = 3
# Output: 4
# Explanation: The longest ideal string is "abcd". The length of this string is
# 4, so 4 is returned.
#
#
# Constraints:
# 1 <= s.length <= 105
# 0 <= k <= 25
# s consists of lowercase English letters.

from itertools import combinations


def longestIdealString(s: str, k: int) -> int:

    # Brute force solution checking every possible combination
    # n = len(s)
    # longest = 0
    #
    # for length in range(1, n + 1):
    #     for subsequence in combinations(s, length):
    #         is_ideal = True
    #         for i in range(1, len(subsequence)):
    #             if abs(ord(subsequence[i]) - ord(subsequence[i - 1])) > k:
    #                 is_ideal = False
    #                 break
    #
    #             if is_ideal:
    #                 longest = max(longest, len(subsequence))
    #
    # return longest

    # cache = {}  # type: ignore
    #
    # def helper(i, prev):
    #     if i == len(s):
    #         return 0
    #
    #     if (i, prev) in cache:
    #         return cache[(i, prev)]
    #
    #     res = helper(i + 1, prev)  # skip s[i]
    #
    #     if prev == "" or abs(ord(s[i]) - ord(prev)) <= k:
    #         res = max(res, 1 + helper(i + 1, s[i]))  # include s[i]
    #
    #     cache[(i, prev)] = res
    #
    #     return res
    #
    # return helper(0, "")

    # optimal dp solution
    dp = [0] * 26

    for c in s:
        cur = ord(c) - ord("a")
        longest = 1

        for prev in range(26):
            if abs(cur - prev) <= k:
                longest = max(longest, 1 + dp[prev])

        dp[cur] = max(dp[cur], longest)
    return max(dp)
