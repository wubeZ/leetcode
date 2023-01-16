class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        s_stack = []
        e_stack = []
        start, end = newInterval[0], newInterval[1]
        #starting position
        for i in range(len(intervals)):
            if intervals[i][1] < start:
                s_stack.append(intervals[i])
            else:
                start = min(start, intervals[i][0])
                break
        
        
        #ending position
        for i in range(len(intervals)-1,-1,-1):
            if intervals[i][0] > end:
                e_stack.append(intervals[i])
            else:
                end = max(end, intervals[i][1])
                break
        
        s_stack.append([start, end])
        s_stack.extend(e_stack[::-1])
        
        return s_stack