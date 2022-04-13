class Solution:
    def candy(self, ratings: List[int]) -> int:
        ans = [1] * len(ratings)
        in_bound = lambda x: 0 <= x < len(ratings)
        
        for i in range(len(ratings)):
            if in_bound(i - 1) and ratings[i] > ratings[i-1]:
                ans[i] = ans[i - 1] + 1
                
        for j in range(len(ratings)- 1,-1,-1):
            if in_bound(j + 1) and ratings[j] > ratings[j + 1]:
                ans[j] = max(ans[j], ans[j + 1] + 1)
                
        return sum(ans)