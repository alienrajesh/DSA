# leetcode 0019.py Remove N'th node from end

# Given the head of a linked list,
# remove the nth node from the end of the list and
# return its head.

# Exmaple 1 :
# head   = 1 --> 2 --> 3 --> 4 --> 5  , n = 2
# output = 1 --> 2 --> 3 --> 5

# Example 2:
# head = 1 --> 2 , n = 1
# output = 1


# Example 3 : only one element in linked list
# head = 1 , n = 1
# output = None
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Method 1 :
# Reversing the linked list and then removing the given index
# and then again reversing the list


# Method 2:
# using two pointer
class Solution:
    def removeNthFromEnd(self, head: [ListNode], n: int) -> [ListNode]:
        dummy = ListNode(0, head)
        left = dummy
        right = head

        while n > 0 and right:
            right = right.next
            n -= 1

        while right:
            left = left.next
            right = right.next
        
        # removing the node i.e. changing the pointer 
        left.next = left.next.next

        return dummy.next


head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
my_solution = Solution()
removed_list = my_solution.removeNthFromEnd(head, 2)

while removed_list:
    suffix = " --> "
    if not removed_list.next:
        suffix = ""
    print(removed_list.val, end=suffix)
    removed_list = removed_list.next
