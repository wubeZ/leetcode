class Solution:
    def search(self, left, right, intervals, target):
        
        while left + 1 < right:
            mid = left + (right - left)// 2
            
            if intervals[mid][0] < target:
                left = mid
            else:
                right = mid
                
        return intervals[right] if 0 <= right < len(intervals) else -1
        
        
        
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        new_intervals = sorted(intervals)
        
        maps = defaultdict(int)
        
        for i in range(len(intervals)):
            maps[tuple(intervals[i])] = i
        
        ans = []
        n = len(intervals)
        for i in range(n):
            val = self.search(-1, n , new_intervals, intervals[i][1])
            if val != -1:
                val = maps[tuple(val)]
            ans.append(val)
            
        return ans