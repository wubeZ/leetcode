# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        
        def dfs(left, right):
            if left > right:
                return None
            
            
            mid = left + (right - left) // 2
            
            left_child = dfs(left, mid - 1)
            
            right_child = dfs(mid + 1, right)
            
            node = TreeNode(nums[mid])
            node.left = left_child
            node.right = right_child
            
            return node
        
        
        return dfs(0, len(nums)-1)