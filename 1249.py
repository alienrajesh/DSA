# 1249. Minimum Remove to Make Valid Parentheses
#
# Given a string s of '(' , ')' and lowercase English characters.
# Your task is to remove the minimum number of parentheses ( '(' or ')', in any
# positions ) so that
# the resulting parentheses string is valid and return any valid string.
# Formally, a parentheses string is valid if and only if:
# It is the empty string, contains only lowercase characters, or
# It can be written as AB (A concatenated with B), where A and B are valid
# strings, or
# It can be written as (A), where A is a valid string.
#
#
# Example 1:
# Input: s = "lee(t(c)o)de)"
# Output: "lee(t(c)o)de"
# Explanation: "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.
#
#
# Example 2:
# Input: s = "a)b(c)d"
# Output: "ab(c)d"
#
#
# Example 3:
# Input: s = "))(("
# Output: ""
# Explanation: An empty string is also valid.
#
#
# Constraints:
# 1 <= s.length <= 105
# s[i] is either'(' , ')', or lowercase English letter.


def minRemoveToMakeValid(s: str) -> str:

    res = []
    open_brac = 0

    for char in s:

        if char == "(":
            res.append(char)
            open_brac += 1
        elif char == ")" and open_brac > 0:
            res.append(char)
            open_brac -= 1
        elif char != ")":
            res.append(char)

    filetered = []

    for char in res[::-1]:
        if char == "(" and open_brac > 0:
            open_brac -= 1
        else:
            filetered.append(char)

    return "".join(reversed(filetered))
