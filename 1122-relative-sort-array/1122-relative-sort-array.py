class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        counter = Counter(arr1)
        counter2 = Counter(arr2)
        ans = []
        for elem in arr2:
            for _ in range(counter[elem]):
                ans.append(elem)
        
        arr1.sort()
        
        for elem in arr1:
            if elem not in counter2:
                ans.append(elem)
                
        return ans
                