class Solution:
    def trap(self, height: List[int]) -> int:
        maxleft = [0]* (len(height)+1)
        maxright = [0]*(len(height)+1)
        mingap = [0]*len(height)
        
        for i in range(len(height)):
            maxleft[i] = max(maxleft[i-1], height[i])
        for i in range(len(height)-1,-1,-1):
            maxright[i] = max(maxright[i+1], height[i])
        for i in range(len(height)):
            mingap[i] = min(maxleft[i], maxright[i])
        
        ans = 0
        for i in range(len(height)):
            if mingap[i] - height[i] >= 0:
                ans += mingap[i] - height[i]
        
        return ans 