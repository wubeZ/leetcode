class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        lists = []
        ans = []
        
        for num in arr:
            val = abs(num - x)
            lists.append((val,num))
        
        lists.sort()
        for i in range(k):
            ans.append(lists[i][1])
        
        return sorted(ans)