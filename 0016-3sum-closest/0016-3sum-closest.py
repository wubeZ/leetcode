class Solution:
    def threeSumClosest(self, num: List[int], target: int) -> int:
        num.sort()
        result = num[0] + num[1] + num[2]
        for i in range(len(num) - 2):
            j, k = i+1, len(num) - 1
            while j < k:
                sums = num[i] + num[j] + num[k]
                if sums == target:
                    return sums
                
                if abs(sums - target) < abs(result - target):
                    result = sums
                
                if sums < target:
                    j += 1
                elif sums > target:
                    k -= 1
            
        return result
            