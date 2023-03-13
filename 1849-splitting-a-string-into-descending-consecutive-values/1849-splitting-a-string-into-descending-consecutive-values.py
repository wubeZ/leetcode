class Solution:
    def backtrack(self, index, arr, s):
        if index >= len(s)  and len(arr) >= 2:
            return True
        
        for i in range(index, len(s)):
            val = s[index: i + 1]
            
            if len(arr) < 1 or (int(arr[-1]) - int(val) == 1):
                isValid = self.backtrack(i + 1, arr + [val] , s)
                if isValid:
                    return True
        
        return False
                            
            
            
    def splitString(self, s: str) -> bool:
        return self.backtrack(0, [], s)