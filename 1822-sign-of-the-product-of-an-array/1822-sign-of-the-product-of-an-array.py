class Solution:
    def arraySign(self, nums: List[int]) -> int:
        neg_count = 0
        
        for num in nums:
            if num == 0:
                return 0
            neg_count += int(num < 0)
        
        return 1 if neg_count %2 == 0 else -1