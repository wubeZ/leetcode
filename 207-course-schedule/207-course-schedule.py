class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0] * numCourses
        queue, ans = deque(), []
        lists = defaultdict(list)
        
        if len(prerequisites) == 0:
            return True
        
        for i in range(len(prerequisites)):
            indegree[prerequisites[i][1]] += 1
            lists[prerequisites[i][0]].append(prerequisites[i][1])
            
        
        for node in range(numCourses):
            if indegree[node] == 0:
                queue.append(node)
        
        while queue:
            cur = queue.popleft()
            ans.append(cur)
            
            for node in lists[cur]:
                indegree[node] -= 1
                if indegree[node] == 0:
                    queue.append(node)
                        
        return len(ans) == numCourses