class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        leftCount = 0
        rightCount = 0
        stack = []
        
        for i in range(len(nums)):
            while stack and stack[-1] > nums[i]:
                stack.pop()
                leftCount += 1
            stack.append(nums[i])
        
        stack = []
        for i in range(len(nums)-1, -1,-1):
            while stack and stack[-1] < nums[i]:
                stack.pop()
                rightCount += 1
            stack.append(nums[i])
            
        
        count = min(leftCount, rightCount)
            
            
        return count <= 1
        