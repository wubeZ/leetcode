class Solution:
    def findComplement(self, num: int) -> int:
        ans = ""
        while num:
            if num & 1:
                ans = "0" + ans
            else:
                ans = "1" + ans
            num >>= 1
        return int(ans, 2)
            
            