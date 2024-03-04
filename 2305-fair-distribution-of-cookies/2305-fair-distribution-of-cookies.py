class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        buckets = [0] * k
        ans = [float("inf")]
        cookies.sort(reverse = True)
        
        def dfs(idx):
            if idx >= len(cookies):
                ans[0] = min(ans[0], max(buckets))
                return
            
            if max(buckets) > ans[0]:
                return
            
            for i in range(k):
                buckets[i] += cookies[idx]
                dfs(idx + 1)
                buckets[i] -= cookies[idx]
        
        dfs(0)
        
        
        return ans[0]