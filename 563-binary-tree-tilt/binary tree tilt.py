# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        self.total = 0
        
        def dfs(r):
            if not r:
                return 0
            
            left = dfs(r.left)
            right = dfs(r.right)
            
            self.total += abs(left - right)
            
            return left + right + r.val
            
        dfs(root)
        
        return self.total    
            
            
