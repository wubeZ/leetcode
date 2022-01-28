# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fastPointer =  head
        slowPointer = head
        slowcount = 1
        fastcount = 1
        while(fastPointer.next):
            fastPointer = fastPointer.next
            fastcount += 1
            if slowcount == fastcount//2:
                slowPointer = slowPointer.next
                slowcount += 1
        return slowPointer    
    