class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        i = 0
        visited = set()
        while i < len(nums):
            if nums[i] in visited:
                return nums[i]
            visited.add(nums[i])
            i += 1