class Solution:
    def checkValidString(self, s: str) -> bool:
        count = 0
        
        for ch in s:    
            if count <= 0 and ch == ")":
                return False
            elif count > 0 and ch == ")":
                count -= 1
            else:
                count += 1
        
        backcount = 0 
        
        for i in range(len(s)-1,-1,-1):
            if backcount <= 0 and s[i] == "(":
                return False
            if backcount > 0 and s[i] == "(":
                backcount -= 1
            else:
                backcount += 1
            
        return True