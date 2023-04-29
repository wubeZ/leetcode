class Solution:
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        res = [None] * len(queries)
        edgeList.sort(key=lambda x: x[2])
        new_list = [query + [idx] for idx , query in enumerate(queries)]
        queries = sorted( new_list , key=lambda x: x[2])
        
        root = list(range(n))
        
        def find(x):
            if root[x] != x:
                root[x] = find(root[x])
            return root[x]
        
        def union(x, y):
            rx, ry = find(x), find(y)
            if rx != ry:
                root[ry] = rx
                return 
        
        i = 0
        for a, b, limit, idx in queries:
            while i < len(edgeList) and edgeList[i][2] < limit:
                x, y, d = edgeList[i]
                union(x, y)
                i += 1
            res[idx] = find(a) == find(b)   
            
        return res