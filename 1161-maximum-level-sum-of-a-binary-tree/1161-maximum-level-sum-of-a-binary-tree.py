# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        
        queue = deque()
        queue.append((root, 1))
        total_sum = root.val
        ans = 1
        
        
        while queue:
            n = len(queue)
            for i in range(n):
                cur, level = queue.popleft()

                if cur.left:
                    queue.append((cur.left, level + 1))
                if cur.right:
                    queue.append((cur.right, level + 1))
            if not queue:
                break
            sum_nodes = sum([node.val for node, level in queue])
            if total_sum < sum_nodes:
                total_sum = sum_nodes
                ans = level + 1
        
        return ans
        