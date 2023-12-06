class Solution:
    def totalMoney(self, n: int) -> int:
        days = n // 7
        remainder = n % 7
        
        full_week = (days*(28 + 28 + 7 * (days - 1)))// 2
        
        start = (days + 1)
        end = (days + remainder)
        
        remaining = (remainder*(start + end))// 2
        
        
        return full_week + remaining
            
            