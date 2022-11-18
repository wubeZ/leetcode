class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        counter1 = Counter(nums1)
        counter2 = Counter(nums2)
        ans = []
        
        for i in counter1:
            if i in counter2:
                for _ in range(min(counter1[i], counter2[i])):
                    ans.append(i)
    
        return ans