class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        d = defaultdict(set)
        
        for path in paths:
            temp = path.split(" ")
            dire = temp[0]
            for file in temp[1:]:
                temp2 = file.split("(")
                f, k = temp2[0], temp2[1][:-1]
                res = dire +'/'+ f
                d[k].add(res)
        
        ans = []
        for values in d.values():
            if len(values) > 1: 
                ans.append(values)
        
        return ans
                