import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        n = re.sub(r'[^a-z0-9]', '', s.lower())
        left = 0
        right = len(n) - 1

        while left < right:
            if n[left] != n[right]:
                return False
            left += 1
            right -= 1
        return True