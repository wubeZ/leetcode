class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        #first we need to find previous smaller and next smaller
        
        stack = []
        
        prev_smaller = [-1] * len(heights)
        next_smaller = [len(heights)] * len(heights)
        
        for i in range(len(heights)):
            while stack and heights[stack[-1]] > heights[i]:
                top = stack.pop()
                next_smaller[top] = i
                
            if stack:
                prev_smaller[i] = stack[-1]
            
            stack.append(i)
    
        ans  = 0
        for i in range(len(heights)):
            length = heights[i]
            width = (next_smaller[i] - prev_smaller[i] - 1)
            
            area = (length) * (width)
            ans = max(ans, area)
            
        return ans