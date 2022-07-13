class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        queue = deque()
        indegree = [0] * n
        
        for edge in edges:
            graph[edge[0]].append(edge[1])
            indegree[edge[1]] += 1
        
        for i in range(n):
            if indegree[i] == 0:
                queue.append(i)
        
        return queue
            
        