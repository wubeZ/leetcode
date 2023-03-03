class Solution:
    def search(self, nums: List[int], target: int) -> int:
        k = 0
        n = len(nums)
        i = n//2
        while i > 0:
            while k+i < n and nums[i+k] <= target:
                k += i
            i //= 2
            
        return k if nums[k] == target else -1