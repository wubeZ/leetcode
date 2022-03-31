class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        negative_flag = False
        res = 0
        if (dividend > 0 and divisor < 0) or (dividend < 0 and divisor > 0):
            negative_flag = True
        dividend, divisor = abs(dividend), abs(divisor)
        
        while dividend >= divisor:
            temp, i = divisor, 1
            while dividend >= temp:
                dividend -= temp
                res += i
                i <<= 1
                temp <<= 1
                
        if negative_flag:
            res = -res
            if -pow(2,31) < res:
                return res
            return -pow(2,31)
        
        if pow(2,31)-1 < res:
            return pow(2,31)-1
        return res
        