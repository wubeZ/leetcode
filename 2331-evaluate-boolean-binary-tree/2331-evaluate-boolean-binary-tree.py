# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(node):
            if not node.left and not node.right:
                return node.val
            
            left = dfs(node.left)
            right = dfs(node.right)
            if node.val == 2:
                return left or right
            else:
                return left and right
                
        return dfs(root)
        
        