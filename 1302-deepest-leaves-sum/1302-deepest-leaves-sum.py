# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        maxlevel = 0
        ans = 0
        
        def dfs(node, level):
            nonlocal maxlevel, ans
            if not node:
                return
            
            if level > maxlevel:
                maxlevel = level
                ans = node.val
            elif level == maxlevel:
                ans += node.val
            
            dfs(node.left , level + 1)
            dfs(node.right, level + 1)
            
            return ans
        
        return dfs(root, 0)