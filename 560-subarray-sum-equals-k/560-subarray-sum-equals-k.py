class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        total = 0
        count = 0
        seen = defaultdict(int)
        seen[0] = 1
        
        for i in nums:
            total += i
            count += seen[total - k]
            seen[total] += 1
 
        return count