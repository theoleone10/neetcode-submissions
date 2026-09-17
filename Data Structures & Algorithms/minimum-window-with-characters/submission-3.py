class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        need = {}
        for ch in t:
            need[ch] = need.get(ch, 0) + 1

        missing = len(t)  # total chars still needed (with multiplicity)

        best_len = float('inf')
        best_l, best_r = 0, 0

        l = 0
        for r, ch in enumerate(s):
            if ch in need:
                if need[ch] > 0:
                    missing -= 1
                need[ch] -= 1
            else:
                need[ch] = -1  # track extras of chars not in t too, harmless

            while missing == 0:
                if (r - l + 1) < best_len:
                    best_len = r - l + 1
                    best_l, best_r = l, r

                left_ch = s[l]
                need[left_ch] += 1
                if left_ch in need and need[left_ch] > 0:
                    missing += 1
                l += 1

        return s[best_l:best_r + 1] if best_len != float('inf') else ""