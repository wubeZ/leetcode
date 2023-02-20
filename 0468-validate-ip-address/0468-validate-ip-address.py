class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        if not queryIP or queryIP[-1] == "." or queryIP[-1] ==":":
            return "Neither"
        
        def check_hex(word):
            if not word.isalnum() or len(word) > 4:
                return False
            for ch in word:
                if ch not in "0123456789ABCDEFabcdef":
                    return False
            return True
        
        def check_IP4(word):
            if len(word) > 1 and word[0] == "0": 
                return False
            if word.isnumeric() and int(ch) >= 0 and int(ch) <= 255:
                return True
            return False
            
        
        if "." in queryIP:
            c = 0
            for ch in queryIP.split("."):
                if not check_IP4(ch):
                    break
                c += 1
            if c == 4:
                return "IPv4"
            return "Neither"
        
        c = 0
        for ch in queryIP.split(":"):
            if not check_hex(ch):
                break
            c += 1
        if c == 8:
            return "IPv6"
        
        return "Neither"
                
                    