class Solution:
    def convert(self, s: str, numRows: int) -> str:
        step = 2 * numRows - 2
        strlist = []
        
        if numRows == 1:
            return s 
        
        for i in range(numRows):
            for j in range(i, len(s), step):
                strlist.append(s[j])
                if i != 0 and i != numRows-1 and j + step - 2*i < len(s):
                    strlist.append(s[ j + step - 2*i])             
    
        return ''.join(strlist)     