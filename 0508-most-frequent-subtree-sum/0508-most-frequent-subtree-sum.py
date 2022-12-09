# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        counter = defaultdict(int)
        maxfreq = [0]
        
        def dfs(node):
            if not node:
                return 0
            
            left = dfs(node.left)
            right = dfs(node.right)
            
            total = left + right + node.val
            counter[total] += 1
            maxfreq[0] = max(maxfreq[0] , counter[total])
            
            return total
        
        dfs(root)
        res = []
        for k, v in counter.items():
            if v == maxfreq[0]:
                res.append(k)
                
        return res