# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        pointer = root
        
        while pointer:
            if pointer.left:
                leftnode = pointer.left
                
                while leftnode.right: 
                    leftnode = leftnode.right
                
                leftnode.right, pointer.right, pointer.left = pointer.right, pointer.left, None
            
            pointer = pointer.right
        