class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = [0] * numCourses
        lists = defaultdict(list)
        queue, ans = deque(), []
        
        for i in range(len(prerequisites)):
            indegree[prerequisites[i][1]] += 1
            lists[prerequisites[i][0]].append(prerequisites[i][1])
        
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
                        
        while queue:
            cur = queue.popleft()
            ans.append(cur)
            
            for n in lists[cur]:
                indegree[n] -= 1
                if indegree[n] == 0:
                    queue.append(n)
                    
        if numCourses != len(ans):
            return []
        
        return ans[::-1]
            