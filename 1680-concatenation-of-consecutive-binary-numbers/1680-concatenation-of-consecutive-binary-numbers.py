class Solution:
    def concatenatedBinary(self, n: int) -> int:
        ans = 0
        for i in range(1, n+1):
            ans = (ans << (len(bin(i))-2) | i) % (10 ** 9 + 7)
        return ans