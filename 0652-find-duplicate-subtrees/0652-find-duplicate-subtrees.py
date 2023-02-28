# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        
        def dfs(node):
            if not node:
                return
            
            left = dfs(node.left)
            right = dfs(node.right)
            
            cur = f"{node.val},{left},{right}"
            
            if seen[cur] == 1:
                ans.add(node)
            seen[cur] += 1
                
            return cur
            
        seen = defaultdict(int)
        ans = set()
        
        dfs(root)
        
        return ans