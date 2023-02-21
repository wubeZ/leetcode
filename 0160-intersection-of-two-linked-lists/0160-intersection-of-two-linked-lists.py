# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        seen = set()
        
        cur = headA
        
        while cur:
            seen.add(cur)
            cur = cur.next
            
        cur1 = headB
        
        while cur1:
            if cur1 in seen:
                return cur1
            cur1 = cur1.next
        
        return None