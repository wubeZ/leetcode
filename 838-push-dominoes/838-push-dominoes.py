class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        left = list(dominoes)
        right = [dominoes[0]]
        rcount = [0] 
        lcount = [0] * len(dominoes) 
    
        c = 0
        for i in range(1, len(dominoes)):
            if right and right[-1]=="R" and dominoes[i]==".":
                c +=1
                right.append("R") 
            else:
                c = 0
                right.append(dominoes[i])
            rcount.append(c)
            
        c = 0
        for i in range(len(dominoes)-2,-1,-1):
            if left and left[i+1] == "L" and dominoes[i]==".":
                left[i] = "L"
                c +=1
            else:
                left[i] = dominoes[i]
                c = 0
            lcount[i] = c
        
        ans = []
        
        for i in range(len(dominoes)):
            if left[i] == right[i]:
                ans.append(left[i])
            elif left[i]=="." and right[i] !=".":
                ans.append(right[i])
            elif right[i]=="." and left[i] !=".":
                ans.append(left[i])
            else:
                if lcount[i] < rcount[i]:
                    ans.append(left[i])
                elif lcount[i] > rcount[i]:
                    ans.append(right[i])
                else:
                    ans.append(".")
                    
        return "".join(ans)