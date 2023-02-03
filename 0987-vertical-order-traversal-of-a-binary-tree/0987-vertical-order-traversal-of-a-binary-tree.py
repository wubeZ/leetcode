# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def dfs(self, node, level, rows):
        if not node:
            return
        if node.left:
            self.dfs(node.left, level - 1, rows + 1)
        if node.right:
            self.dfs(node.right, level + 1, rows + 1)
        
        self.order[level].append([rows, node.val])
        
        
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.order = defaultdict(list)
        
        self.dfs(root, 0, 1)
        
        ans = []
        for key in sorted(self.order):
            self.order[key].sort()
            val = [node for row, node in sorted(self.order[key])]
            ans.append(val)
        
        return ans