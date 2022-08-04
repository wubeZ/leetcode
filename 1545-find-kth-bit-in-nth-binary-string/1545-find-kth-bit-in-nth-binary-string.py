class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        s = "0"
        
        def invert(s):
            res = ""
            for i in s:
                if i == "0":
                    res += "1"
                else:
                    res += "0"
            return res
        
        i = 0
        while i < n-1:
            rs = invert(s)[::-1]
            s = s + "1" + rs 
            i += 1
            
        return s[k-1]