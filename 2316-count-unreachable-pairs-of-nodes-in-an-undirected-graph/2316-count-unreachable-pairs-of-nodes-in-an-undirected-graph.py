class Solution:
    
    
    def find(self, x):
        if self.parent[x] == x:
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
    
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        self.parent = [i for i in range(n)]
        self.size = [1 for i in range(n)]
        
        
        for a, b in edges:
            self.union(a, b)
            
        for i in range(n):
            self.find(i)
        
        if len(set(self.parent)) == 1:
            return 0
        
        counter = Counter(self.parent)
        countedItems = list(counter.values())
        ans = 0
        
        first = countedItems[0]
        
        for i in range(1, len(countedItems)):
            ans += countedItems[i] * first
            first += countedItems[i]
        
        return ans