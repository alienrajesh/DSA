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

# print(checkInclusion(s1,s2))    



# M 2 : might sort both of them and check if presen in there : XXX wrong XXX




# M 3 : a window the size of s1 and track if all elements are in that window 


def checkInclusion2( s1: str, s2: str) -> bool:
    if len(s1) > len(s2) : 
        return False

    s1count , s2count = [0]*26 , [0]*26
    
    for i in range(len(s1)):
        s1count[ord(s1[i])- ord("a")] += 1
        s2count[ord(s2[i])- ord("a")] += 1
    
    matches = 0
    for i in range(26):
        matches += 1 if s1count[i] == s2count[i] else 0
    l = 0
    for r in range(len(s1),len(s2)):
        if matches == 26:
            return True
        
        index = ord(s2[r]) - ord("a")
        
        s2count[index] +=1
        
        if s1count[index] == s2count[index] :
            matches +=1
        elif s1count[index] +1 == s2count[index] :
            matches -=1
        
        index = ord(s2[l]) - ord("a")
        s2count[index] -=1
        
        if s1count[index] == s2count[index] :
            matches +=1
        elif s1count[index] - 1 == s2count[index] :
            matches -=1
        
        l +=1
        
    return matches == 26

print(checkInclusion2(s1 , s2) )            