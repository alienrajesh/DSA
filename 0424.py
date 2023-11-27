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


s = "ABAB" 
k = 2


def  characterReplacement(s:str , k : int) -> int:
    l , r = 0 , 1
    
    max_length = 0
    
    while r < len(s) :
        curr_length = 0
        
        while s[l] == s[r] :
            curr_length +=1
        
        l = r 
        r +=1
        
        
        
        
        
               