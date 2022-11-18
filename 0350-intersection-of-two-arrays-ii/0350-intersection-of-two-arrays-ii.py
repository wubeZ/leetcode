class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        counter1 = Counter(nums1)
        counter2 = Counter(nums2)
        ans = []
        if len(counter1) >= len(counter2):
            keys = counter2.keys()
        else:
            keys = counter1.keys()
        
        for k in keys:
            if k in counter2 and k in counter1:
                for _ in range(min(counter1[k], counter2[k])):
                    ans.append(k)
    
        return ans