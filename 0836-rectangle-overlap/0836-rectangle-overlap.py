class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        intersection_area = 0
        
        horizontal = [max(rec1[0], rec2[0]),  min(rec1[2], rec2[2])]
        vertical = [max(rec1[1],rec2[1]),  min(rec1[3], rec2[3])]
        
        horizontal_diff = horizontal[1] - horizontal[0] 
        
        vertical_diff =  vertical[1] - vertical[0]
        
        intersection_area = horizontal_diff * vertical_diff
        
        if horizontal_diff <= 0 or vertical_diff <= 0:
            intersection_area = 0
            
        return intersection_area > 0
        
        