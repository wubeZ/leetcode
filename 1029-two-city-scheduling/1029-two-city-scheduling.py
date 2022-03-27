class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int: 
        ans = [] 
        min_cost = 0
        
        for acost, bcost in costs:
            ans.append(bcost - acost)
            min_cost += acost

        ans.sort()
        
        for i in range(len(costs)//2):
            min_cost += ans[i]
        
        return min_cost
            