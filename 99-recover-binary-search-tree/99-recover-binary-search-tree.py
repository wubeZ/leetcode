# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        ans = []
        def inorder(node):
            if not node:
                return 
            inorder(node.left)
            ans.append(node)
            inorder(node.right)
            return ans
    
        inorder(root)
        
        lp = 0
        rp = len(ans) -1
        
        while lp < len(ans):
            if ans[lp].val > ans[lp+1].val:
                break
            lp += 1
        
        while rp < len(ans):
            if ans[rp].val < ans[rp -1].val:
                break
            rp -= 1
        
        ans[lp].val,ans[rp].val = ans[rp].val,ans[lp].val
        
        