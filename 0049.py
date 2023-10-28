import collections

#Input: strs = ["eat","tea","tan","ate","nat","bat"]
#Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

strs = ["eat","tea","tan","ate","nat","bat"]


def groupAnagrams(strs:list[str]) -> list[list[str]]:
    anagram_map = collections.defaultdict(list)
    for w in strs:
       count = [0]*26 
       for i in w:
           count[ord(i)- ord('a')] +=1
       anagram_map[tuple(count)].append(w)
    return anagram_map.values() 




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
           
groupAnagrams1(strs)           
           
        
    
    
       
       




