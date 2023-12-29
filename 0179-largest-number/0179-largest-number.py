class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        
        def comp(a, b):
            return int(a + b) > int(b + a)
        
        nums = list(map(str, nums))
        
        for i in range(len(nums)):
            for j in range(len(nums) - i - 1):
                if not comp(nums[j], nums[j+1]):
                    nums[j+1], nums[j] = nums[j], nums[j+1]
        
        
        return str(int("".join(nums)))