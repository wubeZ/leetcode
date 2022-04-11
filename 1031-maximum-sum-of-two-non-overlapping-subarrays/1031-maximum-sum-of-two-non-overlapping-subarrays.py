class Solution:
    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        maxsum = 0
        for i in range(len(nums) - firstLen + 1):
            sums = sum(nums[i:i+firstLen])
            for j in range(len(nums) - secondLen + 1):
                if j + secondLen - 1 < i or i + firstLen - 1 < j:
                    maxsum = max(maxsum, sums + sum(nums[j:j+secondLen]))
        
        return maxsum