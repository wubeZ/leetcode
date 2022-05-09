class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        timePoints.sort()
        
        zlists = list(zip(timePoints, timePoints[1:] + [timePoints[0]]))
        
        time1, time2 = timePoints[0], timePoints[-1]
        min1 = 60 * int(time1[:2]) + int(time1[3:]) + 1440
        min2 = 60 * int(time2[:2]) + int(time2[3:])
        ans = abs(min1 - min2)
        
        for t1, t2 in zlists:
            min1 = 60 * int(t1[:2]) + int(t1[3:])
            min2 = 60 * int(t2[:2]) + int(t2[3:])
            ans = min(ans, abs(min1 - min2))
            
        return ans