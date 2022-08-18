class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        graph = defaultdict(list)
        
        for i in range(len(edges)):
            s, e = edges[i]
            graph[s].append((e, succProb[i]))
            graph[e].append((s, succProb[i]))
        
        dis = [0] * n
        
        queue = deque()
        queue.append((start,1))
        dis[start] = 1
        
        
        while queue:
            
            node, prob = queue.popleft()
            if prob < dis[node]:
                continue
            
            dis[node] = prob
            
            for child, p in graph[node]:
                if p * prob > dis[child]:
                    queue.append((child, p * prob))
                    
        return dis[end]