class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        counter = defaultdict(int)
        ans = 0
        for num in nums:
            if num in counter:
                ans += counter[num]
            counter[num] += 1
        
        return ans
        
        