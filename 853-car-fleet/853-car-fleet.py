class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        d = {}
        for i in range(len(speed)):
            d[position[i]] = speed[i]
        position.sort()
        
        for j in position:
            dist = (target - j) / d[j]
            
            while stack and (stack[-1] <= dist):
                stack.pop()    
            stack.append(dist)
            
        return len(stack)
            
        
        