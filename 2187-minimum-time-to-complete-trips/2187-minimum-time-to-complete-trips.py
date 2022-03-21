class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        left = 0
        right = max(time) * totalTrips
        best = 0
        while left <= right:
            mid = left + (right - left)//2
            sums = 0
            for i in time:
                sums += mid//i
            
            if sums < totalTrips:
                left = mid + 1
            else:
                best = mid
                right = mid - 1
            
        return best