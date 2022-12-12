# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        
        dummy = TreeNode(0, root)
        
        def delete(node):
            if not node:
                return True
            
            left = delete(node.left)
            right = delete(node.right)
            
            if left:
                node.left = None
            if right:
                node.right = None
                
            return node.val == target and left and right
        
        delete(dummy)
        
        return dummy.left