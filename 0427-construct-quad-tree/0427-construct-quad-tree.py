"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        
        
        def construct_range(top, left, l):
            if l == 1:
                return Node(grid[top][left], True)
            
            topLeft = construct_range(top, left, l // 2)
            topRight = construct_range(top, left + l // 2, l // 2)
            botLeft = construct_range(top + l // 2, left, l // 2)
            botRight = construct_range(top + l // 2, left + l // 2, l // 2)

            children = [topLeft, topRight, botLeft, botRight]
            
            isValid = True
            for child in children:
                if not child.isLeaf or child.val != topLeft.val:
                    isValid = False
                    break
            
            if isValid:
                return Node(topLeft.val, True)
            
            return Node(0, False, topLeft, topRight, botLeft, botRight)
        
        return construct_range(0, 0, len(grid))
        