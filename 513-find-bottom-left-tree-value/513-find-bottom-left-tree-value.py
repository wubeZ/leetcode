# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        queue = deque([root])
        result = []
        while queue:
            temp = [x.val for x in queue]
            result.append(temp)
            n = len(queue)
            i = 0
            while i < n:
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

                i += 1
        
        return result[-1][0]
























# if not root.left and not root.right:
#             return root.val
        
#         self.res = 0
#         def dfs(node, level, maxlevel):
#             if not node:
#                 return
    
#             if node.left:
#                 if not node.left.left and not node.left.right:
#                     if maxlevel <= level:
#                         maxlevel = level
#                         self.res = node.left.val
                
#             dfs(node.left,level+1,maxlevel)
#             dfs(node.right, level+1,maxlevel)
            
#             return self.res
        
#         dfs(root,0,0) 
        
#         return self.res