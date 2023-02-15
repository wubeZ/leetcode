class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        nums = 0
        n = len(num)
        for i in range(n):
            nums += num[n-i-1] * 10**i
        
        ans = nums + k
        
        return [int(ch) for ch in str(ans)]
        