class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        graph = defaultdict(list)
        self.ans = 0
        for i in range(1,len(s)):
            graph[parent[i]].append(i)
        
        def dfs(idx):
            if idx not in graph:
                return 0
            arr = []
            for child in graph[idx]:
                count = dfs(child)
                if s[idx] != s[child]:
                    arr.append(count + 1)
            arr.sort()
            val = 0
            if len(arr) >= 2:
                val = arr[-1] + arr[-2]
            else:
                val = arr[-1] if len(arr) > 0 else 0
            
            self.ans = max(self.ans, val)
            
            return arr[-1] if len(arr) > 0 else 0
        
        
        dfs(0)
        return self.ans + 1