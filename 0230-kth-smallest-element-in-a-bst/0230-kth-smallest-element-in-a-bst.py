# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = [0]
        
        def solve(node, k):
            if not node:
                return -1
            
            left = solve(node.left, k)
            count[0] += 1
            if count[0] == k:
                return node.val
            right = solve(node.right, k)
            
            return max(left, right)
        
        
        return solve(root, k)