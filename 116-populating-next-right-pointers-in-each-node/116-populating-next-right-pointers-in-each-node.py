"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        
        if not root:
            return None
        
        q = deque([root])
        
        while q:
            n = len(q)
            i = 0
            while i < n:
                cur = q.popleft()
                
                if q and i < n-1:
                    cur.next = q[0]
                else:
                    cur.next = None
            
                if cur.left: q.append(cur.left)
                if cur.right: q.append(cur.right)
                
                i += 1
        
        return root
        