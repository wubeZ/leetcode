# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        if len(nums) == 0:
            return None
        
        max_idx = 0
        max_val = 0
        
        for i in range(len(nums)):
            if max_val < nums[i]:
                max_idx = i
                max_val = nums[i]

        node = TreeNode(nums[max_idx])

        node.left = self.constructMaximumBinaryTree(nums[:max_idx])
        node.right = self.constructMaximumBinaryTree(nums[max_idx+1:])
        
        return node