class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort(reverse=True)
        sub = 0
        ans = 0
        for i in range(len(happiness)):
            if k == 0 or (happiness[i] - sub) <= 0:
                break
            
            happiness[i] -= sub
            ans += happiness[i]
            sub += 1
            k -= 1
            
        
        return ans
            
                