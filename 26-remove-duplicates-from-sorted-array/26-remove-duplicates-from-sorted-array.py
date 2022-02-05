class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        spointer, pointer = 0, float("inf")
        for val in nums:
            if val != pointer:
                nums[spointer] = val
                spointer += 1
            pointer = val
        return spointer