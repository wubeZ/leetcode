class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return [[]]
        next_result = self.subsets(nums[1:])
        cur_result = []
        
        for val in next_result:
            cur_result.append([nums[0]]+ val)
            
        return (next_result + cur_result)
