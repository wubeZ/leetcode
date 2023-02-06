class DetectSquares:

    def __init__(self):
        self.cordinates = defaultdict(int)

    def add(self, point: List[int]) -> None:
        self.cordinates[(point[0], point[1])] += 1

    def count(self, point: List[int]) -> int:
        gx, gy = point[0], point[1]
        count  = 0
        for points in self.cordinates:
            x, y = points
            if gy == y and x != gx:
                sidelength = abs(x - gx)
                if (x, y + sidelength) in self.cordinates and \
                (gx, gy + sidelength) in self.cordinates:
                    count += self.cordinates[(x, y + sidelength)] * \
                    self.cordinates[(gx, gy + sidelength)] * self.cordinates[(x, y)]
                if (x, y - sidelength) in self.cordinates and \
                (gx, gy - sidelength) in self.cordinates:
                    count += self.cordinates[(x, y - sidelength)] * \
                    self.cordinates[(gx, gy - sidelength)] * self.cordinates[(x, y)]
        
        return count
                
                    
                    
                    
            
            
            
        


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)