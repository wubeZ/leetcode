class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        adjlist = defaultdict(list)
        
        for i in range(len(nums)):
            adjlist[i].append(nums[i])
        
        def dfs(cur, memo):
            if cur in visited:
                return
            if cur in memo: return memo[cur]
            visited.add(cur)
            for child in adjlist[cur]:
                if child not in visited:
                    self.count += 1
                    dfs(child, memo)
            memo[cur] = self.count
            return
        
        res = float("-inf")
        memo = {}
        for i in range(len(nums)):
            visited = set()
            self.count = 1
            dfs(i, memo)
            res = max(res, self.count)
        
        return res