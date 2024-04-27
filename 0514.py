# 514. Freedom Trail
#
# In the video game Fallout 4, the quest "Road to Freedom" requires players to
# reach a metal dial called the "Freedom Trail Ring" and use the dial to spell
# a specific keyword to open the door.
# Given a string ring that represents the code engraved on the outer ring and
# another string key that represents the keyword that needs to be spelled,
# return the minimum number of steps to spell all the characters in the
# keyword.
# Initially, the first character of the ring is aligned at the "12:00"
# direction. You should spell all the characters in key one by one by rotating
# ring clockwise or anticlockwise to make each character of the string key
# aligned at the "12:00" direction and then by pressing the center button.
#
# At the stage of rotating the ring to spell the key character key[i]:
# You can rotate the ring clockwise or anticlockwise by one place, which counts
# as one step. The final purpose of the rotation is to align one of ring's
# characters at the "12:00" direction, where this character must equal key[i].
# If the character key[i] has been aligned at the "12:00" direction, press the
# center button to spell, which also counts as one step. After the pressing,
# you could begin to spell the next character in the key (next stage).
# Otherwise, you have finished all the spelling.
#
#
# Example 1:
#        G
#     G     O
#   N         D
#    I       D
#
#
# Input: ring = "godding", key = "gd"
# Output: 4
# Explanation:
# For the first key character 'g', since it is already in place, we just need 1
# step to spell this character.
# For the second key character 'd', we need to rotate the ring "godding"
# anticlockwise by two steps to make it become "ddinggo".
# Also, we need 1 more step for spelling.
# So the final output is 4.
#
#
# Example 2:
# Input: ring = "godding", key = "godding"
# Output: 13
#
#
# Constraints:
# 1 <= ring.length, key.length <= 100
# ring and key consist of only lower case English letters.
# It is guaranteed that key could always be spelled by rotating ring.


class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        # t = O(r^2 * k) ,  s --> O(r*k)
        # cache = {}  # type: ignore
        #
        # def helper(r, k):  # r - index at ring
        #
        #     if k == len(key):
        #         return 0
        #
        #     if (r, k) in cache:
        #         return cache[(r, k)]
        #
        #     res = float("inf")
        #
        #     for i, c in enumerate(ring):
        #         if c == key[k]:
        #             min_dist = min(abs(r - i), len(ring) - abs(r - i))
        #             res = min(res, min_dist + 1 + helper(i, k + 1))
        #     cache[(r, k)] = res
        #
        #     return res
        #
        # return helper(0, 0)

        # DP
        # t -> O() s -> O(r)

        dp = [0] * len(ring)

        for k in reversed(range(len(key))):
            next_dp = [float("inf")] * len(ring)

            for r in range(len(ring)):
                for i, c in enumerate(ring):
                    if c == key[k]:
                        min_dist = min(abs(r - i), len(ring) - abs(r - i))
                        next_dp[r] = min(next_dp[r], min_dist + 1 + dp[i])

            dp = next_dp

        return dp[0]
