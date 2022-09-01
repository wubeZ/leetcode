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
            if node.val >= ref:
                self.count += 1
            if node.left:
                dfs(node.left, max(ref, node.left.val))
            if node.right:
                dfs(node.right, max(ref, node.right.val))
            
        dfs(root, root.val)
        return self.count