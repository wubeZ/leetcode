class Solution:
    def intToRoman(self, num: int) -> str:
        
        string = str(num)
        ans = []
        
        for i in range(len(string)):
            power = len(string) - (i+1)
            
            needed = int(string[i]) * (10**(power))
            
            if power == 0:
                if needed == 4:
                    cur = "IV"
                elif needed == 9:
                    cur = "IX"
                else:
                    if needed < 4:
                        cur = "I" * needed
                    else:
                        cur = "V" + ("I" * (needed - 5))
            elif power == 1:
                if needed == 40:
                    cur = "XL"
                elif needed == 90:
                    cur = "XC"
                else:
                    if needed < 40:
                        cur = "X" * (needed//10)
                    else:
                        cur = "L" + ("X" * ((needed - 50)//10))
                        print(needed - 50)
                
            elif power == 2:
                if needed == 400:
                    cur = "CD"
                elif needed == 900:
                    cur = "CM"
                else:
                    if needed < 400:
                        cur = "C" * (needed//100)
                    else:
                        cur = "D" + ("C" * ((needed - 500)//100))
                
            else:
                cur = "M" * (needed//1000) 
            
            ans.append(cur)
        
        return "".join(ans)
            