# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        
        total = 0
        
        def solve(root):
            nonlocal total
            
            if not root:
                return 0
            
            if root.left:
                if not root.left.left and not root.left.right:
                    total += root.left.val
                solve(root.left)
            if root.right:
                solve(root.right)

        
        solve(root)
        return total