class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        
        ans = 0
        idx = 0
        while True:
            
            if idx == len(tickets):
                idx = 0
            
            if tickets[idx] > 0:
                ans += 1
                tickets[idx] -= 1
                
            if tickets[k] == 0:
                break
            
            idx += 1
            
        return ans