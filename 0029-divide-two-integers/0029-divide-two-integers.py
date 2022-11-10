class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        res = 0
        if dividend < 0 and divisor < 0:
            negFlag = True
        elif dividend > 0 and divisor > 0:
            negFlag = True
        else:
            negFlag = False
            
        
        dividend = abs(dividend)
        divisor = abs(divisor)
        
        for i in range(31, -1, -1):
            if divisor << i <= dividend:
                dividend -= divisor << i
                res += 1 << i
        
        ans = res if negFlag else -1*res
        if ans > 2**31 - 1:
            return 2**31 - 1
        elif ans < -2**31:
            return -2**31
        
        return ans