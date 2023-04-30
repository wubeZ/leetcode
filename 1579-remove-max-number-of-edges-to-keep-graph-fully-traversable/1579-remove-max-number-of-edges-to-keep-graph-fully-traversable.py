class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n + 1)]
        self.size = [1 for _ in range(n + 1)]
        self.count = n
    
    def find(self, x):
        if self.parent[x] == x:
            return x
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, a, b):
        pa = self.find(a)
        pb = self.find(b)
        if pa == pb:
            return False
        if self.size[pa]> self.size[pb]:
            self.size[pa] += self.size[pb]
            self.parent[pb] = pa
        else:
            self.size[pb] += self.size[pa]
            self.parent[pa] = pb

        return True
    
class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        ufa = UnionFind(n)
        ufb = UnionFind(n)
        cnta = 0
        common = 0
        
        for edge in edges:
            if edge[0] == 3:
                if ufa.find(edge[1]) != ufa.find(edge[2]):
                    ufa.union(edge[1], edge[2])
                    common += 1
                    cnta += 1
        
        for edge in edges:
            if edge[0] == 1:
                if ufa.find(edge[1])!=ufa.find(edge[2]):
                    ufa.union(edge[1], edge[2])
                    cnta += 1
        
        
        if cnta != n-1:
            return -1
        
        cntb = 0
        for edge in edges:
            if edge[0] == 3:
                if ufb.find(edge[1])!=ufb.find(edge[2]):
                    ufb.union(edge[1], edge[2])
        
        for edge in edges:
            if edge[0] == 2:
                if ufb.find(edge[1])!=ufb.find(edge[2]):
                    ufb.union(edge[1], edge[2])
                    cntb += 1
        
        
        if cntb  + common != n-1:
            return -1
        
        
        total = len(edges)
        
        return total - (cnta + cntb) 