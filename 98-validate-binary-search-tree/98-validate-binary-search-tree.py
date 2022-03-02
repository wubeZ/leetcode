# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        stack = []
        def trav(r):
            if not r:
                return    
            trav(r.left)
            stack.append(r.val)
            trav(r.right)
            
        trav(root)
        return (stack == sorted(stack)) and len(set(stack)) == len(stack)
        
        
        
       