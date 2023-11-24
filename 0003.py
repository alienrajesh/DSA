
#3. Longest Substring Without Repeating Characters

# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.

s = "abcabcbb"

# way to check if the next string added to the sequence length is already present

def lengthOfLongestSubstring(s:str) -> int:
    l , r = 0 , 1
    
    max_length = 1
    length = 1
    strs = ""
    while r < len(s) :
        if s[l] == s[r] or s[r] in strs :
            l = r 
            length = 1
            strs = s[l]
        else:
            length +=1
            strs += s[r] 
        print(strs)
        print(length)
        max_length = max(length, max_length)
        
        r += 1
    return max_length
print(lengthOfLongestSubstring(s))





