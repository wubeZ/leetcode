class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        left, right = 0, len(nums)-1
        
        def helper(n):
            count = 0
            for num in nums:
                if num <= n:
                    count += 1
            
            return count <= n
        
        while left + 1 < right:
            mid = left + (right - left)//2
            if helper(mid):
                left = mid
            else:
                right = mid
                
        return right
            