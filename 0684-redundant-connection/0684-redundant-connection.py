class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parents = [i for i in range(len(edges)+1)]
        size = [1 for i in range(len(edges)+1)]

        def find(x):
            if x == parents[x]:
                return x
            return find(parents[x])

        def union(a, b):
            parent_a = find(a)
            parent_b = find(b)            
            
            if parent_a != parent_b:
                if size[parent_a] >= size[parent_b]:
                    parents[parent_b] = parent_a
                    size[parent_a] += size[parent_b]
                else:
                    parents[parent_a] = parent_b
                    size[parent_b] += size[parent_a]
                return True
            
            return False
        
        
        ans = []
        for a, b in edges:
            isValid = union(a,b)
            if not isValid:
                ans = [a,b]
                
        return ans