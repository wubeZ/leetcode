# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pointer = head
        seen = set()
        dup = set()
        if not head or not head.next: 
            return head  
        
        while pointer:
            if pointer.val not in seen and pointer.val not in dup:
                seen.add(pointer.val)
            else: 
                dup.add(pointer.val)
                while pointer.val in seen:
                    seen.discard(pointer.val)
            pointer = pointer.next
        seen = list(seen)
        seen.sort()
        if not seen:
            return None
        
        head = ListNode(seen[0])
        cur = head

        i = 1
        while i < len(seen):
            node = ListNode(seen[i])
            cur.next = node
            cur = cur.next
            i += 1
            
        return head
                
        
        
        
        