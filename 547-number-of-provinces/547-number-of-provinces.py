class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = [False]*n
        province = 0
        
        def dfs(start):
            visited[start] = True
            for i ,con in enumerate(isConnected[start]):
                if con == 1 and not visited[i]:
                    dfs(i)            
        
        for i in range(n):
            if not visited[i]:
                province += 1
                dfs(i)
        
        return province
        