class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        numset = set(nums)
        if 0 in numset:
            return len(numset) - 1 
        return len(numset)