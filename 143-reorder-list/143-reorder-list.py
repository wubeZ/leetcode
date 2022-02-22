# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        queue = deque()  
        pointer = head
        spointer = head
        
        while pointer:
            queue.append(pointer.val)
            pointer = pointer.next
        
        i = 0
        while spointer:
            if i % 2 == 0:
                spointer.val = queue.popleft()
            else:
                spointer.val = queue.pop()
            i += 1
            spointer = spointer.next
            
        return head