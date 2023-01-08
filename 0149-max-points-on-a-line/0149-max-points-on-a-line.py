class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        xmaps = defaultdict(set)
        ymaps = defaultdict(set)
        
        ans = 0
        for i in range(len(points)-1):
            maps = defaultdict(int)
            max_count = 0
            for j in range(i+1, len(points)):
                if points[i][0] == points[j][0]:
                    xmaps[points[i][0]].add((points[i][0], points[i][1]))
                    xmaps[points[i][0]].add((points[j][0], points[j][1]))
                elif points[i][1] == points[j][1]:
                    ymaps[points[i][1]].add((points[i][0], points[i][1]))
                    ymaps[points[i][1]].add((points[j][0], points[j][1]))
                else:
                    slope = (points[i][1] - points[j][1]) / (points[i][0] - points[j][0])
                    maps[slope] += 1
                    max_count = max(max_count, maps[slope])
            ans = max(ans, max_count)
        
        ans += 1
        for k, val in xmaps.items():
            ans = max(ans, len(val))
        for k, val in ymaps.items():
            ans = max(ans, len(val))
        
        
        
        return ans