class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        j, i = 0, 0
        while j < len(t) and i < len(s):
            if t[j] == s[i]:
                j += 1
            i += 1

        return len(t) - j