class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        losers = defaultdict(int)
        keys = set()
        for win , lose in matches:
            losers[lose] += 1
            keys.add(win)
            keys.add(lose)
        
        ans = [[], []]
        for key in keys:
            if key not in losers:
                ans[0].append(key)
            elif losers[key] == 1:
                ans[1].append(key)
        
        
        return [sorted(ans[0]), sorted(ans[1])]