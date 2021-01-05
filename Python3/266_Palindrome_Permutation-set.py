class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        odd = set()
        for c in s:
            if c not in odd:
                odd.add(c)
            else:
                odd.remove(c)
        return True if len(odd) < 2 else False