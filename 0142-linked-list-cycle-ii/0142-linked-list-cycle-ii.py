# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head
        
        if not head:
            return head
        
        while True:
            slow = slow.next
            
            if not fast.next or not fast.next.next:
                return None
                
            fast = fast.next.next
        
            if slow == fast:
                break
            
        start = head
        
        while start != slow:
            start = start.next
            slow = slow.next
        
        return slow