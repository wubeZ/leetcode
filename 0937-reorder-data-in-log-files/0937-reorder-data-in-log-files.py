class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letters = []
        digits = []
        for i in range(len(logs)):
            log = logs[i]
            newlog = log.split(" ")
            if newlog[-1][-1] in "0123456789":
                digits.append(log)
            else:
                combined = " ".join(newlog[1:])
                letters.append([combined, newlog[0]])
        
        letters.sort()
        
        ans = []
        for i in range(len(letters)):
            val = letters[i][1] + " " + letters[i][0]
            ans.append(val)
        
        ans.extend(digits)
        
        return ans