class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = []
        first_number = float("inf")
        
        for num in nums:
            
            while stack and stack[-1][0] <= num:
                stack.pop()
            
            if stack and stack[-1][1] < num:
                return True
            
            stack.append((num, first_number))
            
            first_number = min(first_number, num)
            
            
        return False
            