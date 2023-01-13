class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        graph = defaultdict(list)
        
        for i in range(1, len(parent)):
            graph[parent[i]].append(i)
        
        ans = [0]
        
        def findlongest(node):
            if node not in graph:
                return 0
            
            arr = []
            count = 0
            
            for child in graph[node]:
                count = findlongest(child)
                if s[child] != s[node]:
                    arr.append(count + 1)
            
            arr.sort()
            val = 0
            
            if len(arr) > 1:
                val = arr[-1] + arr[-2]
            elif len(arr) == 1:
                val = arr[-1] 
                
            ans[0] = max(ans[0], val)
            
            if len(arr) > 0:
                return arr[-1]
            
            return 0
        
        findlongest(0)
        
        return ans[0] + 1