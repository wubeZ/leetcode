# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans = 0
        
        queue = deque([(0, root)]) 
        
        while queue:
            nodes = []
            n = len(queue)
            for _ in range(n):
                idx, node = queue.popleft()
                nodes.append(idx)
                
                if node.left:
                    queue.append((2*idx + 1 , node.left))
                
                if node.right:
                    queue.append((2*idx + 2 , node.right))
            
            rightmost, leftmost = max(nodes), min(nodes)
            ans = max(ans, rightmost - leftmost + 1)
        
        return ans