# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        ptr = dummy
        ptr2 = head
        
        while ptr2:
            if ptr2.val == val:
                ptr2 = ptr2.next
            else:
                ptr.next = ptr2 
                ptr = ptr.next
                ptr2 = ptr2.next
        
        ptr.next = ptr2
        
        return dummy.next
        