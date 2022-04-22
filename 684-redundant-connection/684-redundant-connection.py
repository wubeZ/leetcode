class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = [i for i in range(len(edges)+1)]
        rank = [1 for i in range(len(edges)+1)]
        res = []
        
        def find(x):
            if parent[x] == x:
                return x
            parent[x] = find(parent[x])
            return parent[x]
        
        def union(x,y):
            x = find(x)
            y = find(y)
            if x == y:
                return False
            if rank[x] >= rank[y]:
                parent[y] = x
                rank[x] += rank[y]
            else:
                parent[x] = y
                rank[y] += rank[x]
            return True
        
        for i,j in edges:
            valid = union(i,j)    
            if not valid:
                res = [i,j]
        
        return res
            