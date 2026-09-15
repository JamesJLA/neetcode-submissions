class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        c1 = {}
        c2 = {}
        for i in range(len(s)):
            c1[s[i]] = c1.get(s[i], 0) + 1 
            c2[t[i]] = c2.get(t[i], 0) + 1 
       
        return c1 == c2