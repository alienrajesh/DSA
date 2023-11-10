# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.

s = "race a car"

def isPalindrome(s: str) -> bool:
    l_com_s =(''.join(i for i in s if i.isalnum())).lower()
    rev_s = ""
    for i in range(len(l_com_s) -1, -1 ,-1):
        rev_s += l_com_s[i]
    if l_com_s == rev_s:
        return True
    return False    
    
print(isPalindrome(s))    
    
#amanaplanacanalpanama    