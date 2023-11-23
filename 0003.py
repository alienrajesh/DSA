
#3. Longest Substring Without Repeating Characters

# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.

s = "abcabcbb"

def lengthOfLongestSubstring(s:str) -> int:
    l , r = 0 , 1
    
    l_seq = 0
    length = 0
    while r < len(s):
        
        if s[l] == s[r]:
            l = r
            r +=1
            length =0
        else:
            length +=1
            r +=1 
        l_seq = max(length,l_seq)           
    return l_seq 

print(lengthOfLongestSubstring(s))