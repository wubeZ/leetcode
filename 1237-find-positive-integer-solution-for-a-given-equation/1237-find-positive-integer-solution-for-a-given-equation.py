"""
   This is the custom function interface.
   You should not implement it, or speculate about its implementation
   class CustomFunction:
       # Returns f(x, y) for any given positive integers x and y.
       # Note that f(x, y) is increasing with respect to both x and y.
       # i.e. f(x, y) < f(x + 1, y), f(x, y) < f(x, y + 1)
       def f(self, x, y):
  
"""

class Solution:
    def findSolution(self, customfunction: 'CustomFunction', z: int) -> List[List[int]]:
        left, right = 1, 1000
        ans = []
        
        while left <= 1000:
            
            while right > 1 and customfunction.f(left,right) > z:
                right -= 1
            if customfunction.f(left,right) == z:
                ans.append([left,right])
            
            left += 1
        
        return ans
            
                