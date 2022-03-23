class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        start, end = 0, 0
        d = {}
        ans = []
        for i in range(len(s)):
            if s[i] in d:
                end = i
                d[s[i]][1] = end
            else:
                start = end = i
                d[s[i]] = [start, end]
        
        lists = list(d.values())
        
        start = lists[0][0]
        end = lists[0][1]
        
        for i in range(1, len(lists)):
            if lists[i][0] <= end:
                end = max(end, lists[i][1])
            elif end < lists[i][0]:
                ans.append(end - start + 1)
                start = lists[i][0]
                end = lists[i][1]

        ans.append(end - start + 1)
        
        return ans
        
        
        