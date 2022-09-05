# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def check(p, q):
            if not p and not q: return True
            if (not p and q) or (not q and p): return False
            if p.val != q.val: return False
            
            return check(p.left, q.left) and check(p.right, q.right)
        
        
        
        def dfs(node,subnode):
            if not node and subnode: return False
            
            if node.val == subnode.val and check(node, subnode):
                return True
                
            return dfs(node.left, subnode) or dfs(node.right, subnode)
            
            
        return dfs(root, subRoot)
        