# leetcode - 0021.py "Merge Two Sorted Linked List"


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: [ListNode], list2: [ListNode]) -> [ListNode]:
        dummy = ListNode()
        tail = dummy
        
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next 
            tail = tail.next 
        
        if list1:
            tail.next = list1
        elif list1:
            tail.next = list2
        
        return dummy.next
    
    
list1 = ListNode(1,ListNode(2,ListNode(3,ListNode(4))))
list2 = ListNode(2,ListNode(3,ListNode(5,ListNode(8))))
                
    
my_solution = Solution()
merged_list = my_solution.mergeTwoLists(list1,list2)
     
while merged_list:
    suffix = " --> "
    if not merged_list.next:
        suffix = ""
    print(merged_list.val,end = suffix)
    merged_list = merged_list.next
