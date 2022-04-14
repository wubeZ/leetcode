# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        ans = []
        
        def dfs(node):
            if not node:
                return
            if node.val == val:
                ans.append(node)
                return
            dfs(node.left)
            dfs(node.right)
            
            return
        
        dfs(root)
        
        if len(ans) == 0:
            return None
        
        return ans[0]