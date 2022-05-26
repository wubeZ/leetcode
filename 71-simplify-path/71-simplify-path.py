class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        path = path.split("/")
            
        for i in range(len(path)):
            cur = path[i]
            if cur:
                if cur[0] == "." and len(set(cur)) == 1:
                    if stack and len(cur) == 2:
                        stack.pop()
                    elif len(cur) > 2:
                        stack.append(cur)
                else:
                    stack.append(cur)

        return "/" + "/".join(stack)
        