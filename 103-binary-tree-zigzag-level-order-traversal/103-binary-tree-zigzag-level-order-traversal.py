# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        queue = deque([root])
        res = []
        level = 0
        while queue:
            level += 1
            n = len(queue)
            temp = []
            i = 0
            while i < n:
                cur = queue.popleft()
                temp.append(cur.val)
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
                i += 1
                
            if level %2 == 1:
                res.append(temp)
            else:
                res.append(temp[::-1])
                

        return res
        
        
        