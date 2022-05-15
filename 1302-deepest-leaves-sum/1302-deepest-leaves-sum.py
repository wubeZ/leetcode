# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        queue = deque()
        ans = 0
        queue.append(root)
        while queue:
            lists = [i.val for i in queue]
            ans = sum(lists)
            n = len(queue)
            i = 0
            while i < n:
                cur = queue.popleft()
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
                i += 1
        
        return ans