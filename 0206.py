# leetcode 0206.py "Reversed Linked list"

# Example 1:


# Input: head = [1,2,3,4,5]
# Output: [5,4,3,2,1]


# Example 2:

# Input: head = [1,2]
# Output: [2,1]


# Example 3:

# Input: head = []
# Output: []

# Method 1:
# iterating every object in the given linked list and making another linkedlist
# inserting at the begining of the newLinkedList

# # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# class Solution:
#     def reverseList(self, head: [ListNode]) -> [ListNode]:

#         if head == None or head.next == None :
#             return head


#         itr = head
#         root = LinkedList()
#         while itr :
#             root.insert_at_begining(itr.val)
#             itr = itr.next

#         return root.start

# class LinkedList:

#     def __init__(self) -> None:
#         self.start = None

#     def insert_at_begining(self,data) -> None:

#         node = ListNode(data,self.start)
#         self.start = node


# Method 2 :
#   reversing the direction of pointer
#   given LL = 25 --> 20 --> 12 --> 15 --> 10 --> 5 --> 0
#   new LL   = 25 <-- 20 <-- 12 <-- 15 <-- 10 <-- 5 <-- 0
#   the new LL is reversed . this is more efficient
# two pointer prev - null   curr ptr  - first node


# NEETCODE  solution
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# class Solution:

def reverseList(head: [ListNode]) -> [ListNode]:
    prev , curr = None , head

    # iteratively  # T - O(n) S - O(1)
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt

    return prev

        # Recursive    T - O(n)  S - O(n)

        # if not head:
        #     return None

        # newhead = head

        # if head.next:
        #     newhead = self.reverseList(head.next)
        #     head.next.next = head

        # head.next = None

        # return newhead

l1 =  ListNode(1,ListNode(2,ListNode(4,ListNode(5,ListNode(7,ListNode(9,ListNode(11)))))))
reversedlist = reverseList(l1)

while reversedlist:
    suffix = " --> "
    if not reversedlist.next:
        suffix = ""
    print(reversedlist.val,end=suffix)
    reversedlist = reversedlist.next