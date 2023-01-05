class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key = lambda x : x[1])
        arrows = 1
        end = points[0][1]
        
        for i in range(1, len(points)):
            if end >= points[i][0] and end <= points[i][1]:
                continue
            
            arrows += 1
            end = points[i][1]
        
        
        return arrows