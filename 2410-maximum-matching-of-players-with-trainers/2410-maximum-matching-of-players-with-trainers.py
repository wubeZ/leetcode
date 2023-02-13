class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        
        ans = 0
        idx1, idx2 = 0 , 0
        
        while idx1 < len(players) and idx2 < len(trainers):
            if players[idx1] > trainers[idx2]:
                idx2 += 1
            else:
                ans += 1
                idx1 += 1
                idx2 += 1
        
        
        return ans
                