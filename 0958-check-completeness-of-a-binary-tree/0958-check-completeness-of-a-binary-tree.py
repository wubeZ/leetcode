# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def __init__(self):
        self.ans = True
        self.max_height = 0
        self.min_height = 101
    
    def traverse(self, node, height):
        if not node:
            return height
        
        right = self.traverse(node.right, height + 1)
        
        if self.max_height > right:
            self.ans = False
        
        left = self.traverse(node.left, height + 1)
        
        if self.max_height > left:
            self.ans = False
        
        self.max_height = max(self.max_height, left, right)
        self.min_height = min(self.min_height, left, right)
        
        if abs(self.max_height - self.min_height) > 1:
            self.ans = False
            
        return left
        
    
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        
        self.traverse(root, 0)
        
        return self.ans