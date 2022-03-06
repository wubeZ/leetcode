# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        if self.trav(root) != float("inf"):
            return True
        else:
            return False
        
    def trav(self, r):
            if not r:
                return 0

            left = self.trav(r.left) 
            right = self.trav(r.right)
            
            if abs(left - right) <= 1:
                return max(left, right) + 1
            
            return float("inf")
        
    
    
        