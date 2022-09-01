# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.count = 0
        
        def dfs(node, ref):
            if not node:
                return
            
            if node.val >= ref:
                self.count += 1
                
            if node.left and node.left.val >= ref:
                dfs(node.left, node.left.val)
            else:
                dfs(node.left, ref)
                
            if node.right and node.right.val >= ref:
                dfs(node.right, node.right.val)
            else:
                dfs(node.right, ref)
            
        dfs(root, root.val)
        return self.count