# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        
        def dfs(node, nextNode):
            if not node:
                return nextNode
            
            result = dfs(node.left, node)
            node.left = None
            node.right = dfs(node.right, nextNode)
            
            return result
        
        return dfs(root, None)
        