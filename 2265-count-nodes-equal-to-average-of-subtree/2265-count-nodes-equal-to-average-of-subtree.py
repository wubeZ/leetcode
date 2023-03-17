# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def traverse(self, node):
        if not node:
            return 0, 0
        
        left = self.traverse(node.left)
        
        right = self.traverse(node.right)
        
        total = left[0] + right[0] + node.val
        number = left[1] + right[1] + 1

        if node.val == (total//number):
            self.ans += 1
            
        return (total, number)
        
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        val = self.traverse(root)
        
        return self.ans