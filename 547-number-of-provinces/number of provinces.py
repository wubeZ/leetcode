class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        parent = [ i for i in range(len(isConnected)*len(isConnected))]
        rank = [1] * (len(isConnected) * len(isConnected))
        self.size = len(isConnected)
        
        def findset(x):
            if x == parent[x]:
                return x
            
            parent[x] = findset(parent[x])
            return parent[x]
        
        def unionset(x,y):
            x = findset(x)
            y = findset(y)
            
            if x != y:
                if rank[x] > rank[y]:
                    parent[y] = x
                elif rank[x] < rank[y]:
                    parent[x] = y
                else:
                    parent[x] = y
                    rank[x] += 1
                self.size -= 1
        
        for i in range(len(isConnected)):
            for j in range(len(isConnected[0])):
                if i != j and isConnected[i][j] == 1:
                    unionset(i,j)
                
                    
        return self.size
        
