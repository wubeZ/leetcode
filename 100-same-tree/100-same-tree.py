# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        def trav(r1 , r2):
            if not r1 and not r2:
                return True
            elif not r1:
                return False
            elif not r2:
                return False
            
            if r1.val != r2.val:
                return False
             
            return trav(r1.left,r2.left) and trav(r1.right,r2.right)
        
        return trav(p,q)