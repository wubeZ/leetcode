class Solution:
    def largestValsFromLabels(self, values: List[int], labels: List[int], numWanted: int, useLimit: int) -> int:
        arr = list(zip(values, labels))
        
        arr.sort(reverse = True)
        
        ans = 0
        counter = defaultdict(int)
        count = 0
        
        for i in range(len(arr)):
            if count == numWanted:
                break
            if counter[arr[i][1]] < useLimit:
                count += 1
                ans += arr[i][0]
            counter[arr[i][1]] += 1
        
        return ans
            
            