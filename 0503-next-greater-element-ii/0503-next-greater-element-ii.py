class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        length = n * 2
        
        stack = []
        ans = [-1] * len(nums)
        
        for i in range(length):
            idx = i % n
            while stack and nums[stack[-1]] < nums[idx]:
                top = stack.pop()
                ans[top] = nums[idx]
                
            stack.append(idx)
        
        return ans