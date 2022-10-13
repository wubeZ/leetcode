# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        prev = float("-inf")
        def check(node):
            nonlocal ans, prev
            if not node: return 0
            check(node.left)
            if prev >= node.val:
                ans = False
            else:
                prev = node.val
            check(node.right)
            
        ans = True
        check(root)
        return ans 
                
            
            