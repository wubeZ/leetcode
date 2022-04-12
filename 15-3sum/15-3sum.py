class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left, right = i+1, len(nums)-1
            while left < right:
                sums = nums[i] + nums[left] + nums[right]
                if sums < 0:
                    left += 1 
                elif sums > 0:
                    right -= 1
                else:
                    res.append((nums[i], nums[left], nums[right]))
                    left += 1
                    right -= 1
        return list(set(res))
             