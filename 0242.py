from collections import Counter
#Method 1 : counting the number of letter in the given words 
#           comparing them
# This method has  O(n) time  complexity and O(n) space complexity
def isAnagram( s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        countS, countT = {}, {}
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i],0) #.get() is used to get and element from the dictionary
            countT[t[i]] = 1 + countT.get(t[i],0) #when there is no element it returns 0

        return countS == countT
        
#method 2: python has built in function called Counter() that does what
#           we have done in method 1
# But in interview the interviewer might ask how how to code this counter function
#Code of method 2:
def isAnagram( s: str, t: str) -> bool:
    
    return Counter(s) == Counter(t) 

 
 
 
 
# method 3: by sorting the two strings 
# this has a down side,time complexity will be different according to the sorted algorithms used

def isAnagram( s: str, t: str) -> bool:
    
    return sorted(s) == sorted(t)



s , t= "anagram" ,"nagaram"

def isAnagram4(s:str , t:str) ->bool:
    if len(s) != len(t):
        return False
    
    groupS, groupT = {} , {}
    
    for i in range(len(s)):
        groupS[s[i]] = 1 + groupS.get(s[i],0)
        groupT[t[i]] = 1 + groupT.get(t[i],0)
    print(groupT)
    print(groupS)
    return groupS == groupT
    
print(isAnagram4(s, t))