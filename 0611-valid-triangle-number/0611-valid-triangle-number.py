class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        ans = 0
        nums.sort()
        
        
        for i in range(len(nums)-1,-1,-1):
            l = 0
            r = i - 1
            
            while l < r:
                if nums[l] + nums[r] > nums[i]:
                    ans += r - l
                    r -= 1
                else:
                    l += 1
            
        
        return ans
                    
                    