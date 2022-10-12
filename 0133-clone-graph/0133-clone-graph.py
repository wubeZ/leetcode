"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node: return None
        visited = set()
        newNode = Node(node.val)
        cloned  = {node:newNode}
        
        ans = ptr = newNode
        
        def dfs(cur, ptr):
            for n in cur.neighbors:
                if n not in cloned:
                    newN = Node(n.val)
                    cloned[n] = newN
                    ptr.neighbors.append(newN)        
                    dfs(n, newN)
                else:
                    ptr.neighbors.append(cloned[n])
                    
        dfs(node, ptr)
        return ans