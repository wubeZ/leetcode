class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        pointer, spointer = 0, 0
        
        while len(nums) > spointer:
            if nums[pointer] != nums[spointer]:
                nums[pointer + 1] = nums[spointer]
                pointer += 1
            spointer += 1
        
        return pointer + 1