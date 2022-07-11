# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans, levels = [], []
        queue = deque()
        queue.append(root)
        if not root:
            return []
        
        while queue:
            levels = [x.val for x in queue]
            ans.append(levels[-1])
            i = 0
            n = len(queue)
            while i < n:
                cur = queue.popleft()
                if cur: 
                    if cur.left:
                        queue.append(cur.left)
                    if cur.right:
                        queue.append(cur.right)

                i += 1
        
        return ans