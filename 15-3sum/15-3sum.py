class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        
        for cur in range(len(nums)-2):
            
            left, right = cur + 1, len(nums)-1
            while left < right:
                sums = nums[cur] + nums[left] + nums[right]
                if sums < 0:
                    left += 1 
                elif sums > 0:
                    right -= 1
                else:
                    res.append((nums[cur], nums[left], nums[right]))
                    left += 1
                    right -= 1
                    
        return list(set(res))
             