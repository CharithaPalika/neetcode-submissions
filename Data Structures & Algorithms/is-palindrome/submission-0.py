class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.replace(" ", "")
        s = ''.join(c.lower() for c in s if c.isalnum())
        # print(s)
        for i in range(len(s)//2):
            # print(i, len(s)-1-i)
            if s[i] != s[len(s)-1-i]:
                return False
            else:
                continue
        return True  
            
        