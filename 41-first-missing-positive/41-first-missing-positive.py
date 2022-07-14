class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums = set([i for i in nums])
        
        res = 1
        
        i = 1
        while True:
            if i not in nums:
                res = i
                break
            i += 1
        
        return res