# Longest Repeating Character Replacement

# Example 1:

# Input: s = "ABAB", k = 2
# Output: 4
# Explanation: Replace the two 'A's with two 'B's or vice versa.


# Example 2:

# Input: s = "AABABBA", k = 1
# Output: 4
# Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
# The substring "BBBB" has the longest repeating letters, which is 4.
# There may exists other ways to achieve this answer too.


s = "AABABBA" 
k = 1

# NEETCODE solution 
# time - O(26*n)
# spcae - O(26)
def  characterReplacement(s:str , k : int) -> int:
    count = {} 
    
    l = 0 
    res = 0
    for r in range(len(s)):
        count[s[r]] = 1 + count.get(s[r],0)
        
        while (r -l +1) - max(count.values()) > k :
            count[s[l]] -= 1     
            l +=1
            
        res = max(res,r-l+1)    
    return res
    

print(characterReplacement(s , k ))


#TODO  new solution needs to implemented with the maxf 