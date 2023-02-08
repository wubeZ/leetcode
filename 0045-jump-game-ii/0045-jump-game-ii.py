class Solution:
    def jump(self, nums: List[int]) -> int:
        ans = 0
        furthest_end = 0
        current_reach = 0
        
        for i in range(len(nums) - 1):
            current_reach = max(current_reach, i + nums[i])
            
            if i == furthest_end:
                ans += 1
                furthest_end = current_reach
        
        return ans