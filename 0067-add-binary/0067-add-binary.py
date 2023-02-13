class Solution:
    def addBinary(self, a: str, b: str) -> str:
        
        bnum = int(b, 2)
        anum = int(a, 2)
        
        total = anum + bnum
        total = bin(total)[2:]
        
        return total
        