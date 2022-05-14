class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        start = intervals[0][0]
        end = intervals[0][1]
        ans = []
        for i in range(1,len(intervals)):
            if end < intervals[i][0]:
                ans.append([start,end])
                start = intervals[i][0]
                end = intervals[i][1]
            elif end <= intervals[i][1]:
                end = intervals[i][1]
                
        ans.append([start,end])
        
        return ans