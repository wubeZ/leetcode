class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = []
        i = 0
        while i <= n:
            ans.append(bin(i).count("1"))
            i += 1
        return ans
        