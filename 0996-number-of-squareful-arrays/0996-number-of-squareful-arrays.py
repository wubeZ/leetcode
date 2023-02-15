class Solution:
    def numSquarefulPerms(self, nums: List[int]) -> int:
        graph = defaultdict(set)
        n = len(nums)
        self.count = 0
        
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j:
                    total = nums[i] + nums[j]
                    isValid = math.sqrt(total) - int(math.sqrt(total))
                    if isValid == 0.0:
                        graph[nums[i]].add((j, nums[j]))
                        graph[nums[j]].add((i, nums[i]))
        
        def dfs(node):
            values_seen = set()
            
            if n == len(seen): 
                self.count += 1
            
            for idx, val in graph[node]:
                if (idx, val) not in seen and val not in values_seen:
                    values_seen.add(val)
                    seen.add((idx, val))
                    dfs(val)
                    seen.remove((idx, val))
        
        visited = set()
        for idx, val in enumerate(nums):
            if val not in visited:
                visited.add(val)
                seen = set()
                seen.add((idx, val))
                dfs(val)
        
        return self.count