# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.word = None
        
    def traverse(self, node, path):
        if not node:
            return 
        
        if not node.left and not node.right:
            path.append(node.val)
            result = [ chr(97 + path[i]) for i in range(len(path))]
            temp = "".join(result[::-1])
            if self.word:
                self.word = min(self.word, temp)
            else:
                self.word = temp
            return
        
        self.traverse(node.left, path + [node.val])
        self.traverse(node.right, path + [node.val])
        
    
        
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        
        self.traverse(root, [])
        
        
        return self.word