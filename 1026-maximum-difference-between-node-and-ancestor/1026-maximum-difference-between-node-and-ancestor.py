# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        
        def dfs(node):
            if not node:
                return (-1, -1)
            
            left = dfs(node.left)
            right = dfs(node.right)
            
            leftmin, leftmax = left
            rightmin, rightmax = right
            
            if (-1,-1) == left and (-1,-1) == right:
                return (node.val, node.val)
            val = 0
            if (-1,-1) != left and (-1,-1) != right:
                val = max(val, abs(node.val - leftmin))
                val = max(val, abs(node.val - leftmax))
                val = max(val, abs(node.val - rightmin))
                val = max(val, abs(node.val - rightmax))
            
            if (-1,-1) == left:
                val = max(val, abs(node.val - rightmin))
                val = max(val, abs(node.val - rightmax))
            if (-1,-1) == right:
                val = max(val, abs(node.val - leftmin))
                val = max(val, abs(node.val - leftmax))
            
            self.ans = max(self.ans, val)
            
            if (-1,-1) == left and (-1,-1) != right:
                return (min(node.val, rightmin), max(node.val, rightmax))
            
            if (-1,-1) != left and (-1,-1) == right:
                return (min(node.val, leftmin), max(node.val, leftmax))
            
            return (min(node.val, leftmin, rightmin), max(node.val, leftmax, rightmax))
        
        dfs(root)
        
        return self.ans