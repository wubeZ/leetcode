# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        levels = []
        queue = deque()
        queue.append(root)
        
        while queue:
            values = [k.val for k in queue]
            levels.append(values)
            temp = deque()
            for i in range(len(queue)):
                cur = queue.popleft()
                if cur.left:
                    temp.append(cur.left)
                if cur.right:
                    temp.append(cur.right)
                
            queue = temp
        
        return levels[::-1]