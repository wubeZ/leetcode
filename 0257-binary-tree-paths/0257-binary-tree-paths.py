# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        path = []
        ans = []
        def dfs(node):
            if not node.left and not node.right:
                path.append(str(node.val))
                ans.append("->".join(path))
                path.pop()
                return 
            
            path.append(str(node.val))
            if node.left:
                dfs(node.left)
            
            if node.right:
                dfs(node.right)
            path.pop()
        
        dfs(root)
        return ans