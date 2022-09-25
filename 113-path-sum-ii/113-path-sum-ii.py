# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        
        def dfs(node, path, sums):
            if node.left:
                dfs(node.left, path + [node.left.val], sums + node.left.val)
            if node.right:
                dfs(node.right, path + [node.right.val], sums + node.right.val)
            if not node.left and not node.right:
                if sums == targetSum:
                    ans.append(path[::])
                    return
                
                
            
        ans = []
        if not root: return ans
        
        dfs(root, [root.val], root.val)
        
        return ans