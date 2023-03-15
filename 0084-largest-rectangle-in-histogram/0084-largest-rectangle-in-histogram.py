class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        stack = []
        
        ans = 0
        
        for i in range(len(heights)):
            while stack and heights[stack[-1]] > heights[i]:
                top = stack.pop()
                
                width = i - 1 - (stack[-1] if stack else -1)
                length = heights[top]
                
                area = length *  width
                ans = max(ans, area)
            
            stack.append(i)
            
            
        while stack:
            top = stack.pop()
            width = len(heights) - 1 - (stack[-1] if stack else -1) 
            length = heights[top]
            
            area = length * width
            ans = max(ans, area)
    
        return ans