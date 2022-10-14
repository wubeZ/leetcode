class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = defaultdict(int)
        adjlist = defaultdict(list)
        
        for i in range(len(prerequisites)):
            a, b = prerequisites[i]
            adjlist[b].append(a)
            indegree[a] += 1
            
        queue = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
        ans = []       
        while queue:
            node = queue.popleft()
            ans.append(node)
            for childNode in adjlist[node]:
                indegree[childNode] -= 1
                if indegree[childNode] == 0:
                    queue.append(childNode)
        
        return ans if len(ans) == numCourses else []
            