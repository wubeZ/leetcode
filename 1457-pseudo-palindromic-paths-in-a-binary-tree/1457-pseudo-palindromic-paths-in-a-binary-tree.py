# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        d = [0] * 10
        
        def check():
            count = 0
            for i in range(len(d)):
                if d[i]%2 != 0: count += 1    
            if count > 1 : return False
            return True
        
        def dfs(node):
            if node:
                d[node.val] += 1
                if not node.left and not node.right:
                    if check(): self.ans += 1
                else:
                    dfs(node.left)
                    dfs(node.right)
                d[node.val] -= 1
                
        dfs(root)
        
        return self.ans