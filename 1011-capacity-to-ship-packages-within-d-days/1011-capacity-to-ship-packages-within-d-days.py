class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left, right = max(weights), sum(weights)
        best = -1

        def check(capacity):
            countdays = curr = 0
            for i in weights:
                if curr + i > capacity:
                    curr = 0
                    countdays += 1
                curr += i
            return countdays + 1
            
        while left <= right:
            mid = left + ((right - left)//2)
            d = check(mid)
            if d <= days:
                best = mid
                right = mid - 1
            else:
                left = mid + 1
        
        return best
                
            