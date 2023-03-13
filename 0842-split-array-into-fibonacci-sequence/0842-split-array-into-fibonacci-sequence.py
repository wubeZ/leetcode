class Solution:
    
    def check(self, val):
        if len(val) > 1 and val[0] == "0":
            return False
        return int(val) < 2**31
        
    def backtrack(self, index, arr, num):
        if index >= len(num) and len(arr) >= 3:
            return (True, list(map(int, arr)) )
        
        for i in range(index, len(num)):
            val = num[index : i + 1]
            if self.check(val) and (len(arr) < 2 or ( int(val) == int(arr[-1]) + int(arr[-2]) ) ):
                isValid = self.backtrack(i + 1, arr + [val], num)
                if isValid[0]:
                    return isValid
        
        return (False, [])
            
    
    def splitIntoFibonacci(self, num: str) -> List[int]:
        
        result = self.backtrack(0, [], num)
        
        return result[1]
                               