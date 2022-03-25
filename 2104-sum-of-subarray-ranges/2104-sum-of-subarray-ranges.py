class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        sums = 0
        
        for i in range(len(nums)):
            for j in range(i,len(nums)):
                if i == j:
                    min_num, max_num = nums[i], nums[i]
                else:
                    max_num = max(max_num, nums[j])
                    min_num = min(min_num, nums[j])
                    sums += (max_num - min_num)
            
        return sums