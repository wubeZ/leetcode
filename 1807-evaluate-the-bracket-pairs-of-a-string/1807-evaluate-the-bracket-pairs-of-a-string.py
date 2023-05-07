class Solution:
    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:
        maps = {}
        ans = []
        for lists in knowledge:
            maps[lists[0]] = lists[1]
        
        l = 0
        r = 0
        
        while r < len(s):
            if s[r] == "(":
                start = r + 1
                while s[r] != ")":
                    r += 1
                end = r 
                if s[start:end] in maps:
                    ans.append(maps[s[start:end]])
                else:
                    ans.append("?")
                r = end
            else:
                ans.append(s[r])
            
            r += 1
        
        return "".join(ans)
                