class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = []
        first_number = float("inf")
        
        for i in range(len(nums)):
            while stack and stack[-1][0] < nums[i]:
                stack.pop()
                
            if stack and stack[-1][0] > nums[i] and stack[-1][1] < nums[i]:
                return True
            
            stack.append((nums[i], first_number))
            
            first_number = min(first_number, nums[i])
            
        
        return False
            