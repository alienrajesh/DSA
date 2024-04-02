# 205. Isomorphic Strings
#
# Given two strings s and t, determine if they are isomorphic.
#
# Two strings s and t are isomorphic if the characters in s can be replaced to
# get t. All occurrences of a character must be replaced with another character
# while preserving the order of characters. No two characters may map to the
# same character, but a character may map to itself.
#
#
# Example 1:
# Input: s = "egg", t = "add"
# Output: true
#
# Example 2:
# Input: s = "foo", t = "bar"
# Output: false
#
# Example 3:
#
# Input: s = "paper", t = "title"
# Output: true
#
#
# Constraints:
# 1 <= s.length <= 5 * 104
# t.length == s.length
# s and t consist of any valid ascii character.


def isIsomorphic(s: str, t: str) -> bool:
    map_st, map_ts = {}, {}

    for i in range(len(s)):
        c1, c2 = s[i], t[i]

        if (c1 in map_st and map_st[c1] != c2) or (c2 in map_ts and map_ts[c2] != c1):
            return False

        map_st[c1] = c2
        map_ts[c2] = c1

    return True
