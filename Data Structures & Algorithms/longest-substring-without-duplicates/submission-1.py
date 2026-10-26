class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        maxs = 0
        chars = set()
        for r in range(len(s)):
            while s[r] in chars:
                chars.remove(s[l])
                l+=1
            chars.add(s[r])
            maxs = max(maxs, r - l + 1)

        return maxs