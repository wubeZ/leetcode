class Solution:
    
    def find(self, x):
        
        if x == self.parent[x]:
            return x
        self.parent[x] = self.find(self.parent[x])
        
        return self.parent[x]
    
    def union(self, x,y):
        
        p_x = self.find(x)
        p_y = self.find(y)
        
        if p_x != p_y:
            
            if p_y >= p_x:
                self.parent[p_y] = p_x
            else:
                self.parent[p_x] = p_y
        
        
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        words = list(s1)
        words.extend(list(s2))
        self.parent = { ch:ch for ch in words}
        ans = []
        
        for i in range(len(s1)):
            self.union(s1[i], s2[i])
        
        for i in range(len(baseStr)):
            ch = baseStr[i]
            if baseStr[i] in self.parent:
                ch = self.find(baseStr[i])
            ans.append(ch)
            
        
        return "".join(ans)
        
        
        
        