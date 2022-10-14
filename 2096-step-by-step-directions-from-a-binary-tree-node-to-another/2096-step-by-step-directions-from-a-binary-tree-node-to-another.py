# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        
        self.start, self.dest = [], []
        def dfs(node, path):
            if not node: return
            if node.val == startValue: self.start = path[::]
            if node.val == destValue: self.dest = path[::]
            path.append("L")        
            dfs(node.left, path)
            path.pop()
            
            path.append("R")
            dfs(node.right, path)
            path.pop()
            
        dfs(root, [])
        
        ans = ""
        i = 0
        while i < len(self.start) and i < len(self.dest):
            if self.start[i] == self.dest[i]:
                i += 1
            else:
                break
        
        ans += ("U" * (len(self.start) - i))
        ans += "".join(self.dest[i:])
        
        return ans 
            
            