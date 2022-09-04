# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        g = collections.defaultdict(list) 
        queue = [(root,0)]
        while queue:
            new = []
            d = collections.defaultdict(list)
            for node, s in queue:
                d[s].append(node.val) 
                if node.left:  new += (node.left, s-1), 
                if node.right: new += (node.right,s+1),  
            for i in d: g[i].extend(sorted(d[i]))
            queue = new
            
        return [g[i] for i in sorted(g)]