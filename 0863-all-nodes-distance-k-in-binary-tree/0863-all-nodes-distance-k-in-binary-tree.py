# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        levels = defaultdict(list)
        
        def find(node, c):
            if not node:
                return
            if c == k:
                levels[k].append(node.val)
                return
            left = find(node.left, c + 1)
            right = find(node.right, c + 1)
        
        
        def dfs(node):
            if not node:
                return -1
            if node.val == target.val:
                find(node, 0)
                return 1
            
            left = dfs(node.left)
            right = dfs(node.right)
            
            if left != -1:
                if left == k:
                    levels[k].append(node.val)
                    return -1
                else:
                    find(node.right, left + 1)
                    return left + 1
            if right != -1:
                if right == k:
                    levels[k].append(node.val)
                    return -1
                else:
                    find(node.left, right + 1)
                    return right + 1
                
            return max(left, right)
            
        dfs(root)
        return levels[k]