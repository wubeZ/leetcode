class Solution:
    
    def find(self, x):
        if x == self.parent[x]:
            return x
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        px = self.find(x)
        py = self.find(y)
        
        if px != py:
            if self.size[px] >= self.size[py]:
                self.parent[py] = px 
                self.size[px] += self.size[py] 
            else:
                self.parent[px] = py
                self.size[py] += self.size[px]
    
    
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0: return 0
        self.parent = {nums[i]:nums[i] for i in range(len(nums))}
        self.size = {nums[i]:1 for i in range(len(nums))}
        
        for i in range(len(nums)):
            if nums[i] in self.parent and (nums[i]+1) in self.parent:
                self.union(nums[i], nums[i]+1)
            if nums[i] in self.parent and (nums[i]-1) in self.parent:
                self.union(nums[i], nums[i]-1)
            
        return max(self.size.values())
            