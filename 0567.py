# 567. Permutation in String

# Example 1:

# Input: s1 = "ab", s2 = "eidbaooo"
# Output: true
# Explanation: s2 contains one permutation of s1 ("ba").
# Example 2:

# Input: s1 = "ab", s2 = "eidboaoo"
# Output: false

# s1 = "ab"
# s2 = "eidbaooo"

s1 = "adc"
s2 = "dcda"

def checkInclusion( s1: str, s2: str) -> bool:
    
    l = 0 
    res = []
    while l < len(s1):
        for r in range(len(s2)):
            if s1[l] in s2[r]:
                res.append(r)
                
        l +=1
    for r in range(len(res)-1):
        if res[r+1] - res[r] == 1 or res[r+1] - res[r] == -1:
            pass
        else:
            return False
    return True

print(checkInclusion(s1,s2))    