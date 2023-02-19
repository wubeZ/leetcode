# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        queue = deque()
        if root:
            queue.append(root)
        
        arr = []
        
        flag = True
        
        while queue:
            vals = [node.val for node in queue]
            
            if flag:
                arr.append(vals)
            else:
                arr.append(vals[::-1])
            
            flag = not flag
            
            n = len(queue)
            for i in range(n):
                cur = queue.popleft()
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
        
        return arr