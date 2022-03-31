class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        ans = []
        n = len(nums)
        if len(nums) < 3:
            return 0
        
        for i in range(n-2):
            count = 1
            diff = nums[i+1] - nums[i]
            for j in range(i+1,n):
                if nums[j] - nums[j-1] == diff:
                    count += 1
                    if count >= 3:
                        ans.append(count)
                else:
                    break
                
        return len(ans)
            
            