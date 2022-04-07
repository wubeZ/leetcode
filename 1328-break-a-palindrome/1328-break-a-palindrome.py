class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        def isPalindrome(string):
            return str(string) == str(string[::-1])
        pal = list(palindrome)
        if len(palindrome) == 1:
            return ""

        for i in range(len(palindrome)):
            if len(palindrome)-1 > i and ord(palindrome[i]) == 97:
                continue
            temp2, val = palindrome[i], 97
            while 97 <= val <= 122:
                pal[i] = chr(val)
                val += 1
                if not isPalindrome(pal):
                    return str("".join(pal))
            pal[i] = temp2
                