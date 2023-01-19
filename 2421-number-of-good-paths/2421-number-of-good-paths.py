class Solution:
    
    def find(self, x):
        if x == self.parent[x]:
            return x
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def numberOfGoodPaths(self, vals: List[int], edges: List[List[int]]) -> int:
        n = len(vals)
        self.parent = {x:x for x in range(n)}
        count = []
        n_edges = []
        res = n
        
        for val in vals:
            count.append(Counter({val: 1}))
        
        for i, j in edges:
            val = max(vals[i], vals[j])
            n_edges.append([val, i, j])
        
        n_edges.sort()

        for val, i, j in n_edges:
            p_i = self.find(i)
            p_j = self.find(j)
            
            cj = count[p_i][val] 
            ci = count[p_j][val]
            
            res += ci * cj
            self.parent[p_j] = p_i
            
            count[p_i] = Counter({val: ci + cj})
            
        return res