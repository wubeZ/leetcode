# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        queue = deque([root])
        ans = []
        
        if not root:
            return []
        
        while queue:
            temp = [x.val for x in queue]
            ans.append(max(temp))
            n = len(queue)
            i = 0
            while i < n:
                node = queue.popleft()
            
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                    
                i += 1
                
        return ans