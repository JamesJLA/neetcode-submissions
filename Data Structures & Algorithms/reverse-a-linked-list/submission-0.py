# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        curr = head
        prev = None
        while curr:
           nxt = curr.next 
           curr.next = prev
           prev = curr
           curr = nxt

        return prev
# for 0 1 2 3 
# we get curr = 0 prev = 0 current = 1 we want for first loop 1 0 2 3
# then 2 1 0 3 then 3 2 1 0