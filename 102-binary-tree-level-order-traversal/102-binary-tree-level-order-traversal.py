# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque()
        res, level = [], []
    
        if not root:
            return []
        
        queue.append(root)
        
        while queue:
            level = [x.val for x in queue]
            res.append(level)
            i , n = 0, len(queue)
            while i < n:
                cur = queue.popleft()
                if cur:
                    if cur.left:
                        queue.append(cur.left)
                    if cur.right:
                        queue.append(cur.right)
                i += 1
                    
                
        return res
        
        