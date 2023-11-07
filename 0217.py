

nums = [1,2,3,1] 


def check(nums):
    hashSet = set()
    for i in nums:
        if i in hashSet:
            return True 
        hashSet.add(i)
    return False
        
        


#another method is to check the length of hashSet and nums
# if len(hashSet) != len(nums) then we return false


#diff method with dictionary

def check2(nums):
    numbers = {}
    for i in nums:
        if i in numbers:
            return True
        numbers[i] = 1
    return False

print(check2(nums))