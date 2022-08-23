class Solution:
    def canJump(self, nums: List[int]) -> bool:
        step = 0
        for i in range(len(nums)-1):
            if nums[i] == 0 and step == 0:
                return False
            step  =  max(step , nums[i])
            step -= 1
        
        return True

            