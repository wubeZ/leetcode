class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        indegree = defaultdict(int)
        
        for a, b in prerequisites:
            graph[b].append(a)
            indegree[a] += 1
        
        queue = deque()
        
        for key in range(numCourses):
            if indegree[key] == 0:
                queue.append(key)
                numCourses -= 1
        
        count = 0
        
        while queue:
            node = queue.popleft()
            
            for next_node in graph[node]:
                indegree[next_node] -= 1
                if indegree[next_node] == 0:
                    del indegree[next_node]
                    count += 1
                    queue.append(next_node)
        
        return numCourses == count