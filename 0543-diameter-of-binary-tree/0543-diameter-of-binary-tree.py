# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans = [0]
        def dfs(node):
            if not node:
                return -1
            if not node.left and not node.right:
                return 0
            
            left = dfs(node.left) + 1
            right = dfs(node.right) + 1
            
            ans[0] = max(ans[0], left + right)
            
            return max(left, right)
        
        
        dfs(root)
        
        return ans[0]