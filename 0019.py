# Given the head of a linked list,
# remove the nth node from the end of the list and 
# return its head.

# Exmaple 1 :
# head   = 1 --> 2 --> 3 --> 4 --> 5  , n = 2
# output = 1 --> 2 --> 3 --> 5 

# Example 2:
# head = 1 --> 2 , n = 1 
# output = 1 

# Example 3 :
# head = 1 , n = 1 
# output = None 


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: [ListNode], n: int) -> [ListNode]:
        pass 





head = ListNode(1,ListNode(2,ListNode(3,ListNode(4,ListNode(5)))))
my_solution = Solution()
removed_list = my_solution.removeNthFromEnd(head)

while removed_list:
    suffix = " --> "
    if  not removed_list.next:
        suffix = ""
    print(removed_list.val,end=suffix)
