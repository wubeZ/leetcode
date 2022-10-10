# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder: return
        if not inorder: return None
        
        node = TreeNode(preorder[0])
        i = inorder.index(preorder[0])
        preorder.pop(0)
        node.left = self.buildTree(preorder, inorder[:i])
        node.right = self.buildTree(preorder, inorder[i+1:])
        
        
        return node
    
            
            
        
        