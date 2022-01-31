# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        pointer = head
        spointer = head
        count = 0    
        while(pointer):
            count += 1
            pointer = pointer.next
            
        if count == n:
            head = head.next
            return head

        elif count == 1:
            head = None
            return head
        
        index = count - n
        scount = 1
        
        while(scount < index):
            scount += 1
            spointer = spointer.next
        
        spointer.next = spointer.next.next
    
        return head