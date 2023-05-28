class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        
        @lru_cache(None)
        def dp(p, m, is_alice):
            if p >= len(piles):
                return 0

            if is_alice:
                return max(dp(p + i, max(m, i), False) + sum(piles[p:p + i]) for i in range(1, 2 * m + 1))
            else:
                return min(dp(p + i, max(m, i), True) for i in range(1, 2 * m + 1))

        return dp(0, 1, True)
            