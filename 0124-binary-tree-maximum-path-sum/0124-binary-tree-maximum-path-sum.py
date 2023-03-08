# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.pathSum = -1003
        
        
    def traverse(self, node):
        if not node:
            return 0
        
        left = self.traverse(node.left)
        right = self.traverse(node.right)
        
        self.pathSum = max(self.pathSum, node.val, node.val + left, node.val + right, node.val + left + right)
        
        return max(node.val + left, node.val + right, node.val)
    
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        self.traverse(root)
        
        return self.pathSum