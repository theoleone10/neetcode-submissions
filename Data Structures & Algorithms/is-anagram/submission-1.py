class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash1 = {}
        hash2 = {}

        n = len(s)

        if len(t) != n:
            return False

        for i in range(n):
            hash1[s[i]] = 1 + hash1.get(s[i],0)
            hash2[t[i]] = 1 + hash2.get(t[i],0)

        return hash1 == hash2