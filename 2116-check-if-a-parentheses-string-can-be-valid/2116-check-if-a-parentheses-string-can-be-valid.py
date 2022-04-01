class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        space = [0]*len(s)
        
        if len(space) % 2:
            return False        
        
        for i,val in enumerate(locked):
            if val == "1":
                if s[i] == "(":
                    space[i] = 1
                else:
                    space[i] = -1
        bal = 0
        left = 0
        for i,val in enumerate(space):
            bal += val
            while left <= i and bal < 0:
                if space[left] == 0:
                    space[left] = 1  
                    bal += 1
                left += 1
            if bal < 0:
                return False
        
        bal = 0
        right = len(space)-1
        for i in range(len(space)-1,-1,-1):
            bal += space[i]
            while right >= i and bal > 0:  
                if space[right] == 0:
                    space[right] = -1
                    bal -= 1
                right -= 1
            if bal > 0:
                return False
            
        return True
        