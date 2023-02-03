class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        for pat in path.split("/"):
            if not pat or pat == ".":
                continue
            elif pat == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(pat)
                
        return "/" + "/".join(stack)
                
        
        
        