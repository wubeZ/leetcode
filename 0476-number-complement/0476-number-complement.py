class Solution:
    def findComplement(self, num: int) -> int:
        res = 0
        shift = 0
        while num:
            flag = num & 1
            if flag == 0:
                x = 1 << shift
                res |= x
            shift += 1
            num >>= 1
        
        return res
            
            