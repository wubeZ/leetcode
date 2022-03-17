class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        left, right = 1, max(nums)
        best = -1
        while left <= right:
            mid = left + (right - left)//2
            arr = [ceil(x/mid) for x in nums]
            if  sum(arr) > threshold:
                left = mid + 1
            elif sum(arr) <= threshold:
                best = mid
                right = mid - 1
        
        return best