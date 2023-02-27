class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        line = [0] * 2052
        
        for i in range(len(logs)):
            line[logs[i][0]] += 1
            line[logs[i][1]] -= 1
        
        prefix = [line[0]]
        
        for i in range(1, len(line)):
            prefix.append(prefix[-1] + line[i])
            
        maxNum = 0
        ans = 0
        
        for i in range(len(prefix)):
            if maxNum < prefix[i]:
                maxNum = prefix[i]
                ans = i
        
        return ans