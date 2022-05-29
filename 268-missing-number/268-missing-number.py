class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = 0
        nums.sort()
        for i in nums:
            if res == i:
                res += 1
            else:
                return res
        
        return res