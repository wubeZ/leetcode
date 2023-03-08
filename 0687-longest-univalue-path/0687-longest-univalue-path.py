# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.maxLength = 0
    
    def traverse(self, node):
        if not node:
            return 0
        
        if not node.left and not node.right:
            return 0
        
        left = self.traverse(node.left)
        right = self.traverse(node.right)
        
        left_count, right_count = 0, 0
        
        if node.left and node.val == node.left.val:
            left_count += left + 1
        
        if node.right and node.val == node.right.val:
            right_count += right + 1
        
        self.maxLength = max(self.maxLength, left_count + right_count)
        
        return max(left_count, right_count)

    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        
        self.traverse(root)
        
        return self.maxLength