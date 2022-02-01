# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        count = 0
        fast = head
        slow = head
        while(fast and fast.next):
            slow = slow.next
            fast = fast.next.next
        
        prev = None
        cur = slow
        
        while cur:
            next_node = cur.next
            cur.next = prev
            prev = cur
            cur = next_node
            
        while prev and head:
            if prev.val != head.val:
                return False
            prev = prev.next
            head = head.next
            
        return True
         
        