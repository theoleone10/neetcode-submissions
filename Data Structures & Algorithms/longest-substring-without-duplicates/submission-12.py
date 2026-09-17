class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        sub = set()
        res = 1

        l, r = 0, 0
        
        while r < len(s):
            if s[r] in sub:
                while s[l] != s[r]:
                    sub.remove(s[l])
                    l += 1
                sub.remove(s[l])
                l += 1
            sub.add(s[r])
            res = max(res, r - l + 1)
            r += 1
        return res
