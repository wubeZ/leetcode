class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        parent = [i for i in range(len(points))]
        rank = [0] * len(points)
    
        def find(x):
            if x == parent[x]:
                return x
            
            parent[x] = find(parent[x])
            return parent[x]
        
        def union(x,y):
            x = find(x)
            y = find(y)
            
            if x == y:
                return False
            else:
                if rank[x] >= rank[y]:
                    rank[x] += rank[y]
                    parent[y] = x
                else:
                    rank[y] += rank[x]
                    parent[x] = y
            return True
        
        distances = []
        
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                dis = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                distances.append((dis,i,j))
                
        distances.sort()
        
        res, count = 0, 0
        for i in range(len(distances)):
            dis, x, y = distances[i]
            if union(x,y) and count < len(points):
                res += dis
                count += 1
                
        return res
                
                
                
            
            
            
            
            
            
        
                
                