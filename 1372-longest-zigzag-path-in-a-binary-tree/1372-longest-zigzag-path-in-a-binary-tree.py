# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        
        def dfs(node, right, total):
            if not node:
                return total
            
            l = dfs(node.left, False, total + 1 if right else 1)
            r = dfs(node.right, True, total + 1 if not right else 1)

            return max(l, r)
        
        ans = dfs(root, None, 0)
        return ans - 1