# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def bst(node, target, res):
            res.append(node)
            if node.val > target:
                bst(node.left, target, res)
            if node.val < target:
                bst(node.right, target, res)
        
            return 
        
        result1, result2 = [], []
        
        bst(root, q.val, result1)
        bst(root, p.val, result2)

        i = 0
        n = min(len(result1), len(result2))
        while i < n:
            if result1[i].val != result2[i].val:
                break
            i += 1
            
        return result1[i-1]
        