"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        ans = []
        if not root: return []
        queue = deque()
        queue.append(root)
        
        while queue:
            ans.append([i.val for i in queue])
            length = len(queue)
            for i in range(length):
                cur = queue.popleft()
                for child in cur.children:
                    if child:
                        queue.append(child)
        
        return ans
            
        