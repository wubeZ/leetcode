class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trusted_count = defaultdict(int)
        trust_count = defaultdict(int)
        
        for a, b in trust:
            trusted_count[a] += 1
            trust_count[b] += 1
        
        for i in range(1, n+1):
            if trust_count[i] == n - 1 and trusted_count[i] == 0:
                return i
            
        
        
        return -1