class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        counter = defaultdict(int)
        
        ans = 0
        l, r = 0, 0
        
        while r < len(nums):
            counter[nums[r]] += 1
            
            while max(counter) - min(counter) > 2:
                counter[nums[l]] -= 1
                if counter[nums[l]] == 0:
                    del counter[nums[l]]
                
                l += 1
                
            ans += r - l + 1
            
            r += 1
        
        
        return ans