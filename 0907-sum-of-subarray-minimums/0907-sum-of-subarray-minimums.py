class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        stack = []
        ans = 0
        mod = 10**9 + 7
        
        for i in range(len(arr)+1):
            
            while stack and (i == len(arr) or arr[stack[-1]] >= arr[i]):
                cur = stack.pop()
                left = -1 if not stack else stack[-1]
                right = i
                count = (cur - left) * (right - cur)
                ans += (count * arr[cur])
            
            stack.append(i)
        
        
        return ans % mod