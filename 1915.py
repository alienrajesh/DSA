# 1915. Number of Wonderful Substrings
#
# A wonderful string is a string where at most one letter appears an odd number
# of times.
# For example, "ccjjc" and "abab" are wonderful, but "ab" is not.
# Given a string word that consists of the first ten lowercase English letters
# ('a' through 'j'), return the number of wonderful non-empty substrings in
# word. If the same substring appears multiple times in word, then count each
# occurrence separately.
#
# A substring is a contiguous sequence of characters in a string.
#
#
#
# Example 1:
#
# Input: word = "aba"
# Output: 4
# Explanation: The four wonderful substrings are underlined below:
# - "aba" -> "a"
# - "aba" -> "b"
# - "aba" -> "a"
# - "aba" -> "aba"
# Example 2:
#
# Input: word = "aabb"
# Output: 9
# Explanation: The nine wonderful substrings are underlined below:
# - "aabb" -> "a"
# - "aabb" -> "aa"
# - "aabb" -> "aab"
# - "aabb" -> "aabb"
# - "aabb" -> "a"
# - "aabb" -> "abb"
# - "aabb" -> "b"
# - "aabb" -> "bb"
# - "aabb" -> "b"
# Example 3:
#
# Input: word = "he"
# Output: 2
# Explanation: The two wonderful substrings are underlined below:
# - "he" -> "h"
# - "he" -> "e"
#
#
# Constraints:
#
# 1 <= word.length <= 105
# word consists of lowercase English letters from 'a' to 'j'.


class Solution:
    def wonderfulSubstrings(self, word: str) -> int:

        # t --> O(N*10) s --> O(2^1024)
        # def convert_to_decimal(binary_mask):
        #     decimal_value = 0
        #     for i, bit in enumerate(binary_mask):
        #         if bit:
        #             decimal_value += 2 ** i
        #     return decimal_value
        #
        # def count_substrings(binary_mask):
        #     decimal_value = convert_to_decimal(binary_mask)
        #     return frequency_map.get(decimal_value, 0)
        #
        # frequency_map = {0: 1}
        # binary_mask = [False] * 10
        # result = 0
        #
        # for char in word:
        #     index = ord(char) - ord('a')
        #     binary_mask[index] = not binary_mask[index]
        #
        #     result += count_substrings(binary_mask)
        #
        #     for i in range(10):
        #         binary_mask[i] = not binary_mask[i]
        #         result += count_substrings(binary_mask)
        #         binary_mask[i] = not binary_mask[i]
        #
        #     decimal_value = convert_to_decimal(binary_mask)
        #     frequency_map[decimal_value] = frequency_map.get(decimal_value, 0) + 1
        #
        # return result

        result = 0
        state = [1] + [0] * 1023
        current = 0

        for char in word:
            index = ord(char) - ord("a")
            current ^= 1 << index

            result += state[current]

            for i in range(10):
                toggled = current ^ (1 << i)
                result += state[toggled]

            state[current] += 1

        return result
