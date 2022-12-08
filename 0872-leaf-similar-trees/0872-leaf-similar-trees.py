# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        
        def dfs(node):
            if not node:
                return 
            
            dfs(node.left)
            dfs(node.right)
            
            if not node.left and not node.right:
                arr.append(node.val)
            
            
        arr = []
        dfs(root1)
        arr1 = arr
        
        arr = []
        dfs(root2)

        return arr1 == arr
        
        