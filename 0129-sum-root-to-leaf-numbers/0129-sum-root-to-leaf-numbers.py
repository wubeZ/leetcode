# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.total = 0
        
    def traverse(self, node, count):
        if not node:
            return 
        
        if not node.left and not node.right:
            count = (count * 10) + node.val
            self.total += count
            
            return 
        
        count = (count * 10) + node.val
        
        self.traverse(node.left, count)
        self.traverse(node.right, count)
        
            
            
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        self.traverse(root, 0)
        
        return self.total