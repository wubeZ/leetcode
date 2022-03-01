class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        num = []
        for nlist in edges:
            for val in nlist:
                num.append(val)
        c = Counter(num)
        
        for key in c:
            if c[key] == len(edges):
                return key