# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        def check(node):
            if not node: return None
            if node.val == val:
                return node
            if node.val > val:
                return check(node.left)
            else:
                return check(node.right)
             
        
        return check(root)