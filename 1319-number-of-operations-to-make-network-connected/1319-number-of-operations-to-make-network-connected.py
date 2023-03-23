class Solution:
        
    def find(self, x):
        if x == self.parent[x]:
            return x
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    
    def union(self, x, y):
        par_x = self.find(x)
        par_y = self.find(y)
        
        if par_x != par_y:
            
            if self.size[par_x] >= self.size[par_y]:
                self.parent[par_y] = par_x
                self.size[par_x] += self.size[par_y]
            else:
                self.parent[par_x] = par_y
                self.size[par_y] += self.size[par_x]
    
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < n - 1:
            return -1
        
        self.parent = [i for i in range(n)]
        self.size = [1 for i in range(n)]
        
        for a, b in connections:
            self.union(a, b)
            
        
        for i, val in enumerate(self.parent):
            self.parent[i] = self.find(self.parent[i])
            
        return len(set(self.parent)) - 1
            
            
            
            