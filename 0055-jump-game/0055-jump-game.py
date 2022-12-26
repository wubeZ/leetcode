class Solution:
    def canJump(self, nums: List[int]) -> bool:
        steps = 0
        for i in range(len(nums)-1):
            if nums[i] == 0 and steps == 0:
                return False
            
            steps = max(steps, nums[i])
            steps -= 1
            
        return True