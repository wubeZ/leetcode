class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        counter = Counter(nums)
        ans = 0
        for i in range(len(nums)):
            if nums[i]-1 not in counter:
                count = 1
                cur = nums[i]
                while cur + 1 in counter:
                    count += 1
                    cur += 1
                ans = max(ans, count)
        
        return ans
            
        
        