# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def __init__(self):
        self.max_height = 0
        self.min_height = 101
    
    def traverse(self, node, height):
        if not node:
            return (height, True)
        
        right = self.traverse(node.right, height + 1)
        
        
        if not right[1] or self.max_height > right[0]:
            return (right[0], False)
        
        left = self.traverse(node.left, height + 1)
        
        if not left[1] or self.max_height > left[0]:
            return (left[0], False)
        
        self.max_height = max(self.max_height, left[0], right[0])
        self.min_height = min(self.min_height, left[0], right[0])
        
        if abs(self.max_height - self.min_height) > 1:
            return (left[0], False)
            
        return left
        
    
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        
        result = self.traverse(root, 0)
        
        return result[1]