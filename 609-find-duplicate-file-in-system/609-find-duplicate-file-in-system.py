class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        d = defaultdict(set)
        
        for path in paths:
            temp = path.split(" ")
            directory = temp[0]
            for file in temp[1:]:
                f, k = file.split("(")
                res = directory +'/'+ f
                d[k].add(res)
        
        return [val for val in d.values() if len(val) > 1]
                