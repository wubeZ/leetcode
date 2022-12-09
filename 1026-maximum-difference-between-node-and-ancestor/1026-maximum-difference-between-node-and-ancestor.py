# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        
        def helper(node, max_val, min_val):
            if not node:
                self.res = max(self.res, max_val - min_val)
                return
            
            helper(node.left, max(max_val, node.val), min(min_val, node.val))
            helper(node.right, max(max_val, node.val), min(min_val, node.val))
        
        helper(root, float('-inf'), float('inf'))
        return self.res