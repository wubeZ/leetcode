class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        standing = sorted(score, reverse=True)
        resp = []
    
        for s in score:
            rank = standing.index(s) + 1
            
            if rank == 1:
                resp.append("Gold Medal")
            elif rank == 2:
                resp.append("Silver Medal")
            elif rank == 3:
                resp.append("Bronze Medal")
            else:
                resp.append(str(rank))
                
        return resp
        