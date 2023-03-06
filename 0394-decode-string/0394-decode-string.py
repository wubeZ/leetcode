class Solution:
    
    def solve(self, s, left, right):
        if s[left] in "0123456789" and s[right] == "]":
            opening = 0
            idx = -1
            
            for i in range(left, right + 1):
                if opening > 1:
                    break
                
                if s[i] == "[":
                    opening += 1
                
                if idx == -1 and s[i] == "[":
                    idx = i
                
            if opening == 1:
                val = s[idx + 1: right] * int(s[left:idx])
                return val
            
            
            
        arr = []

        while left <= right:
            if not s[left] in "0123456789":
                arr.append(s[left])
                left += 1
            else:
                opening = 0
                closing = 0
                idx = -1
                l = left

                while True:

                    if s[left] == "[":
                        opening += 1
                    if idx == -1 and s[left] == "[":
                        idx = left
                    if s[left] == "]":
                        closing += 1

                    if closing > 0 and opening == closing:
                        break
                    
                    if left > right:
                        break
                    
                    left += 1

                val = self.solve(s, idx + 1, left-1)
                res = val * int(s[l:idx])
                left += 1
                arr.append(res)

        return "".join(arr)
                    
        
    def decodeString(self, s: str) -> str:
        
        if s in "0123456789":
            return ""
        
        return self.solve(s, 0, len(s)-1)
        