class Solution:
    def bitwiseComplement(self, n: int) -> int:
        if n == 0: return 1
        ans = ""
        while n:
            if n & 1:
                ans = "0" + ans
            else:
                ans = "1" + ans
            n >>= 1
        return int(ans, 2)