class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        if len(s) > 12:
            return []
        
        
        def backtrack(s,idx):
            if idx == 4:
                if not s:
                    ans.append(".".join(path))
                return
            
            for i in range(1, 4):
                if i <= len(s):
                    
                    if int(s[:i]) <= 255:
                        path.append(s[:i])
                        backtrack(s[i:], idx +1)
                        path.pop()
                        
                    if s[0] == "0":
                        break
        
        
        ans = []
        path = []
        
        backtrack(s,0)
        
        return ans