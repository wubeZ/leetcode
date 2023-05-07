class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        ans = []
        openstack = set()
        delete = set()
        
        for i, ch in enumerate(s):
            if ch in ["(", ")"]:
                if ch == "(":
                    openstack.add(i)
                else:
                    if openstack:
                        openstack.pop()
                    else:
                        delete.add(i)
        
        if delete or openstack:
            for i , ch in enumerate(s):
                if i in openstack or i in delete:
                    continue
                ans.append(ch)
        else:
            ans = s
                
        return "".join(ans)
                        
                    