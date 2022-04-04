# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        pointer = head
        visited = set()
        
        while pointer:
            if pointer in visited:
                return True
            visited.add(pointer)
            pointer = pointer.next
            
        return False