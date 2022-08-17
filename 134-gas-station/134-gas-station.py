class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        prefix = 0
        
        for i in range(len(gas)):
            prefix += (gas[i] - cost[i])
        
        if prefix < 0: return -1
                
        ans, pref = 0, 0
        for i in range(len(gas)):
            pref += gas[i] - cost[i]
            if pref < 0:
                ans = i + 1
                pref = 0
        
        return ans