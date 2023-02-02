class Solution:
    def numberToWords(self, num: int) -> str:
        words = { 1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five", 6: "Six",\
                 7: "Seven", 8: "Eight",9: "Nine", 10: "Ten", 11: "Eleven", 12: "Twelve",\
                 13: "Thirteen", 14: "Fourteen",15: "Fifteen", 16: "Sixteen", \
                 17: "Seventeen", 18: "Eighteen", 19: "Nineteen",20: "Twenty",\
                 30: "Thirty",40: "Forty", 50: "Fifty", 60: "Sixty", 70: "Seventy",\
                 80: "Eighty", 90: "Ninety" }
        
        aboveHundred = ["Thousand","Million","Billion"]
        
        if num == 0:
            return "Zero"
        
        def getWords(n):
            if n == 0:
                return []
            if n < 20:
                return [words[n]]
            if n < 100:
                return [words[(n//10) * 10]] + getWords(n % 10)
            if n < 1000:
                return [words[n//100]] + ['Hundred'] + getWords(n % 100)
            
            for i in range(len(aboveHundred)):
                if n < 1000**(i+2):
                    return getWords(n//(1000**(i+1))) + [aboveHundred[i]] + getWords(n%(1000**(i+1)))
                
        ans = getWords(num)
        
        return " ".join(ans)