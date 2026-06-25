class Solution:
    def longestPalindrome(self, s: str) -> int:
        seen = set()
        result = 0

        for i in range(len(s)):
            if s[i] in seen:
                seen.remove(s[i])
                result += 2
            else:
                seen.add(s[i])

        return result + 1 if seen else result