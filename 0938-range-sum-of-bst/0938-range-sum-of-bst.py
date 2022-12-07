# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        ans = [0]
        def inorder(node):
            if not node:
                return None
            
            inorder(node.left)
            if node.val <= high and node.val >= low:
                ans[0] += node.val
            inorder(node.right)
        
        
        inorder(root)
        
        return ans[0]