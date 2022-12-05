# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        c = 0
        ptr = head
        
        while ptr:
            ptr = ptr.next
            c += 1
        
        mid = c//2
        
        sptr = head
        i = 0
        while i < mid:
            i += 1
            sptr = sptr.next
        
        
        return sptr