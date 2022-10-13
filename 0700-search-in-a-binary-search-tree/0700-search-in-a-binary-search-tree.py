# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        ptr = root
        while ptr:
            if ptr.val == val:
                return ptr
            if ptr.val > val:
                ptr = ptr.left
            elif ptr.val < val:
                ptr = ptr.right
        
        return None