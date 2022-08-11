class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        s, e = newInterval
        start, end = newInterval
        i = 0
        for val in intervals:
            if val[1] < s:
                res.append(val)
                continue
            start = min(val[0], s)
            break
        res1 = []
        for i in range(len(intervals)-1,-1,-1):
            if intervals[i][0] > e:
                res1.append(intervals[i])
                continue
            end = max(intervals[i][1], e)
            break
        
        res.append([start,end])
        
        while res1:
            res.append(res1.pop())
        
        
        return res
            
        
    
            