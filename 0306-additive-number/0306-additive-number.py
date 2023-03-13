class Solution:
    
    def check(self, val):
        res = True
        if len(val) > 1 and val[0] == "0":
            res = False
        return res
    
    def backtrack(self, index, arr, num):
        if index >= len(num) and len(arr) >= 3:
            return True
        
        for i in range(index, len(num)):
            val = num[index : i + 1]
            if self.check(val) and (len(arr) < 2 or int(val) == int(arr[-1]) + int(arr[-2])):
                isValid = self.backtrack(i + 1, arr + [val], num)
                if isValid:
                    return True
        
        return False
        
        
    def isAdditiveNumber(self, num: str) -> bool:
        return self.backtrack(0, [], num)