class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        n = 26
        ans = []
        
        divisor = columnNumber
        
        rem = 0
        while divisor > 0:
            rem = (divisor - 1) % n
            divisor = ((divisor - 1) // n)
            ans.append(rem)
            
        res = []
        for i in range(len(ans)-1,-1,-1):
            res.append(chr(65 + ans[i]))
        
        return "".join(res)
            