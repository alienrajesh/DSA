from collections import defaultdict

#Input: strs = ["eat","tea","tan","ate","nat","bat"]
#Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

strs = ["eat","tea","tan","ate","nat","bat"]


def groupAnagrams(strs:list[str]) -> list[list[str]]:
    anagram_map = defaultdict(list)
    for w in strs:
       count = [0]*26  # a....z
       for i in w:
           count[ord(i)- ord('a')] +=1
       anagram_map[tuple(count)].append(w) # tuple bcoz list can't be key
    return anagram_map.values() # .values() return only the value of the dict



#My solution 

def groupAnagrams1(strs:list[str]) -> list[list[str]]:
    res = []
    groups = {}
    for word in strs:
        key = ''.join(sorted(word))
        if key not in groups:
            groups[key] = [word]
        else:
            groups[key].append(word)
            
    for key in groups:
        res.append(groups[key])   
    return res    
                      
 
 
 
 
 
#Input: strs = ["eat","tea","tan","ate","nat","bat"]
#Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

 
def groupedAnangram2(strs:list[str]) -> list[list[str]]:
    
    res = defaultdict(list)
    
    for s in strs:
        count= [0]*26
        
        for i in s:
            count[ord(i) - ord("a")] +=1
        res[tuple(count)].append(s)    
    return res.values()
                    
print(groupedAnangram2(strs))    
            
# new solution 
#more efficient
# less space

def groupAnagrams4(strs:list[str]) -> list[list[str]]:
    
    myMap = {}
    for word in strs:
        temp = ''.join(sorted(word))
        if temp in myMap:
            myMap[temp].append(word)
        else:
            myMap[temp] = [word]
    return myMap.values()
        
print(groupAnagrams4(strs))



def groupAnagrams5(strs:list[str]) -> list[list[str]] :
    
    res = defaultdict(list)
    
    
    for w in strs:
        count = [0]* 26 
        for i in w:
            count[ord(i)-ord("a")] +=1
        res[tuple(count)].append(w)
    return res.values   
