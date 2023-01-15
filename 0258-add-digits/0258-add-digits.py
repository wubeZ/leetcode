class Solution:
    def addDigits(self, num: int) -> int:
        digit = str(num)
        length = len(digit)
        
        while length != 1:
            temp = 0
            for ch in digit:
                temp += int(ch)
            digit = str(temp)
            length = len(digit)
            
        return int(digit)