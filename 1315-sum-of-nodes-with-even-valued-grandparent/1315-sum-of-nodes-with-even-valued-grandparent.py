# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        self.total = 0
        
        def dfs(r):
            if not r:
                return 0

            if r.val %2 == 0:
                if r.left and r.left.left:
                    self.total += r.left.left.val
                if r.left and r.left.right:
                    self.total += r.left.right.val
                if r.right and r.right.left: 
                    self.total += r.right.left.val
                if r.right and r.right.right:
                    self.total += r.right.right.val
                
            dfs(r.left)
            dfs(r.right)
            
            return 
        
        dfs(root)
        
        return self.total
        
        