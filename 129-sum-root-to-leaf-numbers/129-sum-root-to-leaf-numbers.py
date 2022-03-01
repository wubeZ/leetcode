# Definition for a binary tree node.
# class TreeNode:
#     def init(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.total = 0
        
        def trav(r,n):
            if not r:
                return
            
            n = (n*10) + r.val
            if not r.left and not r.right:
                self.total += n

            trav(r.left, n)
            trav(r.right, n)
            
        trav(root,0)
        
        return self.total