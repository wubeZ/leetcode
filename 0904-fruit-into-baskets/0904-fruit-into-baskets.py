class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        max_size = 1
        
        myset = set()
        l = 0
        last_postion = {}
        
        for r in range(len(fruits)):
            myset.add(fruits[r])
            last_postion[fruits[r]] = r
            
            while len(myset) > 2:
                temp, k = float("inf"), 0
                for key in last_postion:
                    if temp > last_postion[key]:
                        temp = last_postion[key]
                        k = key
                        
                del last_postion[k]
                myset.remove(fruits[temp])
                l = temp + 1
                
            max_size = max(max_size, r - l + 1)
            
        return max_size