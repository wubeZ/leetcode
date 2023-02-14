class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        ordered_set = set()
        n = list(str(n))
        n_temp = sorted(n)
        n = "".join(n_temp)
        
        for i in range(30):
            num = (1 << i)
            num = sorted(list(str(num)))
            ordered_set.add("".join(num))
            
        return n in ordered_set       
        
            
        