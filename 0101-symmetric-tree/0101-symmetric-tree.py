# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        def solve(nodeleft, noderight):
            if not nodeleft and not noderight:
                return True
            if (not nodeleft and noderight) or (not noderight and nodeleft):
                return False
            if nodeleft.val != noderight.val:
                return False
            
            return solve(nodeleft.left, noderight.right) and solve(nodeleft.right, noderight.left)
        
        return solve(root.left, root.right)
        