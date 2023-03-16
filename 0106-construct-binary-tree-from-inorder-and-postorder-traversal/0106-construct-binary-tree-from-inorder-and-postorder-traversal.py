# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:

        def traverse(arr, pos):
            if not arr or not pos:
                return None
            
            node = TreeNode(pos.pop())
            idx = arr.index(node.val)
            
            node.right = traverse(arr[idx+1:], pos)
            
            node.left = traverse(arr[:idx] , pos)
            
            return node
        
        return traverse(inorder, postorder)   
    