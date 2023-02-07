class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        left , window , maxfruit = 0, 0, 0
        d = {}
        
        while left < len(fruits):
            if fruits[left] not in d:
                d[fruits[left]] = 1
            else:
                d[fruits[left]] += 1      
            
            while len(d) > 2:
                d[fruits[window]] -= 1
                if d[fruits[window]] == 0:
                    del d[fruits[window]]
                window += 1
                
            maxfruit = max(maxfruit, left-window +1)
            left += 1
            
        return maxfruit