class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        D = {}
        for i in strs:
            D[i]=[i]
        n = len(strs[0])
        for i in range(len(strs)):
            for j in range(i+1,len(strs)):
                count=0
                for k,l in zip(strs[i],strs[j]):
                    if k!=l:
                        count+=1
                        if count>2:
                            break
                if count==2:
                    D[strs[i]].append(strs[j])
                    D[strs[j]].append(strs[i])
        visited = set()
        comp=0
        for i in D.keys():
            if i not in visited:
                comp+=1
                visited.add(i)
                stack = [i]
                while stack:
                    cur = stack.pop()
                    for new in D[cur]:
                        if new not in visited:
                            visited.add(new)
                            stack.append(new)
        return comp