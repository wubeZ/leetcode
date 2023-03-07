class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = []
        first_number = float("inf")
        
        minArray = []
        min_val = float("inf")
        
        for num in nums:
            min_val = min(min_val, num)
            minArray.append(min_val)
        
        
        for i in range(len(nums)):
            
            while stack and nums[stack[-1]] <= nums[i]:
                stack.pop()
            
            if stack and minArray[stack[-1]] < nums[i]:
                return True
            
            stack.append(i)
            
        return False
            