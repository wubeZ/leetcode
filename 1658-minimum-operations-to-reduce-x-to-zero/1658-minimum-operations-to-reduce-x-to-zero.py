class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        running_start = 0
        end = None
        count = float("inf")
        for i in range(len(nums)):
            if running_start + nums[i] <= x:
                running_start += nums[i]
            else:
                end = i-1
                break
        if end == None and running_start == x:
            return len(nums)
        if end == None and running_start < x:
            return -1
        
        running_end = 0
        j = len(nums)-1
        while j >= 0:
            if running_end + running_start < x:
                running_end += nums[j]
                j -= 1
            elif end >= 0 and running_end + running_start > x:
                running_start -= nums[end]
                end -= 1
            elif running_end + running_start == x:
                count = min(count, (end+1) + (len(nums)-1-j))
                running_end += nums[j]
                j -= 1
            elif running_start == 0 and running_end > x:
                break
                
        return count if count != float('inf') else -1
        
        
            