# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        self.sums = 0
        
        def dfs(node):
            if not node: return 
            
            dfs(node.right)
            self.sums += node.val
            node.val = self.sums
            dfs(node.left)
            
            return node
            
        return dfs(root)
        
        