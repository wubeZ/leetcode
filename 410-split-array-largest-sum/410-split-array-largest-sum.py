class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        
        def canSplit(mid):
            count = 1
            prefixsum = 0
            for n in nums:
                prefixsum += n
                if prefixsum > mid:
                    count += 1
                    prefixsum = n
            
            return count <= m
        
        l, r = max(nums), sum(nums)
        best = r
        
        while l <= r:
            mid = l + (r - l)//2
            
            if canSplit(mid):
                best = mid
                r = mid - 1
            else:
                l = mid + 1
            
        return best