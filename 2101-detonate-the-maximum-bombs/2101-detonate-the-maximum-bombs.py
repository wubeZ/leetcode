class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        adjacency_list = defaultdict(list)
        
        def withInRange(b1,b2):
            dis = pow(( (b1[0]-b2[0])**2 + (b1[1]-b2[1])**2) ,0.5)
            return  dis <= b1[2]
        
        for i in range(len(bombs)):
            for j in range(len(bombs)):
                if i != j and withInRange(bombs[i],bombs[j]):
                    adjacency_list[i].append(j)
        
        def dfs(n, visited):
            count = 1
            for bomb in adjacency_list[n]:
                if bomb not in visited:
                    visited.add(bomb)
                    count += dfs(bomb,visited)
            return count
            
        max_count = 1
        for index in range(len(bombs)):
            visited = set([index])
            count = dfs(index,visited)
            max_count = max(max_count,count)
        
        return max_count
                
            