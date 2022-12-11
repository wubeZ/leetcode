# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.ans = -1001
        def dfs(node):
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            
            subtotal = left + right + node.val
            
            self.ans = max(self.ans, subtotal)
            
            return max(left+node.val,right+node.val, 0)
        
        
        dfs(root)
        
        return self.ans