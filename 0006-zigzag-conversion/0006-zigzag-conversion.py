class Solution:
    def convert(self, s: str, numRows: int) -> str:
        order_dict = defaultdict(list)
        step = numRows - 2
        
        i = 0
        
        while i < len(s):    
            j = 0
            normal = 0
            while i + j < len(s) and normal < numRows:
                order_dict[normal].append(s[i + j])
                j += 1
                normal += 1
            i += j
            k = 0
            step = numRows - 2
            reverse = numRows - 2
            while i + k < len(s)  and step > 0:
                order_dict[reverse].append(s[i + k])
                k += 1
                step -= 1
                reverse -= 1
        
            i += k
        
        ans = ""
        for key in sorted(order_dict):
            ans += "".join(order_dict[key])
        
        return ans
            