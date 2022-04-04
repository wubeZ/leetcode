# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        fpointer = spointer = pointer = head
        count = 0
        
        while pointer:
            count += 1
            pointer = pointer.next
        
        for i in range(k-1):
            spointer = spointer.next
        
        for i in range(count - k):
            fpointer = fpointer.next
        
        spointer.val, fpointer.val = fpointer.val, spointer.val
        
        return head