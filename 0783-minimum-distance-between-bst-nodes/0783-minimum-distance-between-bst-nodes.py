# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        
        def dfs(node):
            if not node:
                return 
            
            arr.append(node.val)
            dfs(node.left)
            dfs(node.right)
            
        
        arr = []
        
        dfs(root)
        
        arr.sort()
        ans = float("inf")
        for i in range(1, len(arr)):
            ans = min(ans, arr[i] - arr[i-1])
        
        return ans
        