class Solution:
    def findComplement(self, num: int) -> int:
        ans = ""
        while num:
            flag = num & 1
            if flag:
                ans = "0" + ans
            else:
                ans = "1" + ans
            num >>= 1
        return int(ans, 2)
            
            