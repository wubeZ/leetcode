# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        mod = 10**9 + 7
        def sums(node):
            if not node:
                return 0
            return sums(node.left) + sums(node.right) + node.val
        
        total = [sums(root)]
        
        def dfs(node):
            if not node:
                return 0
            
            left = dfs(node.left)
            right = dfs(node.right)
            subtotal = left + right + node.val
            self.ans = max(self.ans ,(total[0] - subtotal)*(subtotal))
            return subtotal
        
        dfs(root)
        return self.ans % mod