class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ascii_s = [ord(char) for char in s]
        ascii_t = [ord(char) for char in t]
        ascii_s.sort()
        ascii_t.sort()
        return ascii_s == ascii_t
        