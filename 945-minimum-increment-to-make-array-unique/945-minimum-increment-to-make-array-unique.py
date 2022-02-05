class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        stack = []
        nums.sort()
        count = 0
        
        if len(nums) == 1:
            return 0
    
        for val in nums:
            if len(stack) == 0:
                stack.append(val)
                continue
            if stack[-1] < val:
                stack.append(val)
            elif stack[-1] == val:
                    val += 1
                    stack.append(val)
            elif stack[-1] > val:
                val += (stack[-1] - val)+1
                stack.append(val)
        
        for i in range(len(stack)):
            count += (stack[i] - nums[i])
            
        return count     
            