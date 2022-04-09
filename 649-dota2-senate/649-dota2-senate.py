class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        senate = list(senate)
        
        r_index = deque([i for i in range(len(senate)) if senate[i] == "R"])
        d_index = deque([i for i in range(len(senate)) if senate[i] == "D"])
        
        while r_index and d_index:
            r, d = r_index.popleft(), d_index.popleft()
            
            if r > d:
                d_index.append(len(senate)+d)
            else:
                r_index.append(len(senate)+r)
        
        
        if not r_index:
            return "Dire"
        
        return "Radiant"
            
            