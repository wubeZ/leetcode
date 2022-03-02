# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        def trav(r):
            if not r:
                return
            
            trav(r.left)
            trav(r.right)
            ans.append(r.val)
            
        trav(root)
        
        return ans