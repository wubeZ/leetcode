# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        """
        I need the max height and all the nodes at max height
        
        """
        
        def dfs(node):
            if not node:
                return
            
            val[0] += 1
            if node.left:
                dfs(node.left)
            if node.right:
                dfs(node.right)
            
            
        val = [0]
        dfs(root)
        return val[0]
            
            
            
            
            
        
        