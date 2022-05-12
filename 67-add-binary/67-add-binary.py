class Solution:
    def addBinary(self, a: str, b: str) -> str:
        ans = ""
        cf = 0
        a_len, b_len = len(a) - 1, len(b) - 1
        
        while 0 <= a_len and 0 <= b_len:
            ans += str((int(a[a_len]) ^ int(b[b_len]) ^ cf))
            cf = (int(a[a_len]) & int(b[b_len])) | ((int(a[a_len]) ^ int(b[b_len])) & cf)
            a_len -= 1
            b_len -= 1
            
        
        while 0 <= a_len:
            ans += str((int(a[a_len]) ^ cf))
            cf =  int(a[a_len])*cf
            a_len -= 1
            
        while 0 <= b_len:
            ans += str((int(b[b_len]) ^ cf))
            cf =  int(b[b_len])*cf
            b_len -= 1
        
        
        if cf == 1:
            ans += "1"
        
        return ans[::-1]
    