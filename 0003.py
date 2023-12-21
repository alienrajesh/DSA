
#3. Longest Substring Without Repeating Characters

# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.

s = "abcabcbb"

# way to check if the next string added to the sequence length is already present


def lengthOfLongestSubstring(s:str) -> int:

    charSet = set()
    l = 0
    
    res = 0
    for r in range(len(s)):
        while s[r] in charSet:
            charSet.remove(s[l])
            l+=1
        charSet.add(s[r])
        res = max(res, (r -l) +1)
    return res

# print(lengthOfLongestSubstring(s))

def lengthOfLongestSubstring1(s) -> int:
    charset = set()
    l = 0
    maxlength = 0
    for r in range(len(s)):
        while s[r] in charset :
            charset.remove(s[l])
            l +=1
        charset.add(s[r])
        maxlength = max(maxlength, (r-l) +1)
        
    return maxlength
      
print(lengthOfLongestSubstring1(s))    

