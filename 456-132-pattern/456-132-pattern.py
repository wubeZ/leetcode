class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        if len(nums) < 2:
            return False
        
        stack = []
        num2 = float('-inf')
        
        for i in range(len(nums)-1,-1,-1):
            if nums[i] < num2:
                return True
            while stack and stack[-1] < nums[i]: 
                num2 = stack.pop()
                
            stack.append(nums[i])
            
        return False