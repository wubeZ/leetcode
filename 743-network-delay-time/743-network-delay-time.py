class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        
        for i in range(len(times)):
            start, end , time = times[i]
            graph[start].append((time,end))
        
        dis = [float("inf")] * (n+1)
        dis[0]= 0
        queue = []
        heapq.heappush(queue, (0,k))
        visited = set()
        
        while queue:
            n = len(queue)
            for i in range(n):
                time, cur = heapq.heappop(queue)
                if cur in visited: continue
                visited.add(cur)
                dis[cur] = time
                for i, node in graph[cur]:
                    if node not in visited:
                        heapq.heappush(queue, (time + i, node))
                        
        if max(dis) == float("inf"): return -1
        else:
            return max(dis)