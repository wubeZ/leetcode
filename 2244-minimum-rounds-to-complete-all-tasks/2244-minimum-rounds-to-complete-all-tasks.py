class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        counter = Counter(tasks)
        values = list(counter.values())
        
        def getvalue(num):
            if num %3 == 0:
                return num // 3
            
            if num %3 == 2:
                return (num // 3) + 1
            temp = num
            c = 0
            while num > 0 and num %3 != 0:
                num -= 2
                c += 1
            if num <= 0 and temp %2 == 0:
                return temp // 2
        
            return c + num // 3
            
            
            
        ans = 0
        for i in range(len(values)):
            if values[i] <= 1:
                return -1
            else:
                ans += getvalue(values[i])
        
        
        return ans