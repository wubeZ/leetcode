# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def traverse(self, node, count):
        if not node:
            return 0
        
        if not node.left and not node.right:
            count = (count * 10) + node.val
            return count
        
        count = (count * 10) + node.val
        
        left = self.traverse(node.left, count)
        right = self.traverse(node.right, count)
        
            
        return left + right
            
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        return self.traverse(root, 0)
        