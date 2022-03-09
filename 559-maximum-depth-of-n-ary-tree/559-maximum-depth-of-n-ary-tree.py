"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        
        def dfs(node):
            if not node.children:
                return 1
            count = []
            for i in node.children:
                count.append(dfs(i))
            
            return max(count) + 1
        
        result = dfs(root)
        
        return result
        