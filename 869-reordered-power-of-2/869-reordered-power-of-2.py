class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        num = str(n)
        
        perm = permutations(num)
        
        for p in list(perm):
            if int(p[0]) != 0:
                val = int("".join(p))
                if bin(val).count("1") == 1:
                    return True
        
        return False