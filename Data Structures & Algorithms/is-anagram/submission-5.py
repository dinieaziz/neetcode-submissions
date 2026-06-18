class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Edge case if is not equal
        if len(s) != len(t):
            return False

        # Track the freq of chars
        sSeen, tSeen = {}, {}

        for i in range(len(s)):
            sSeen[s[i]] = 1 + sSeen.get(s[i], 0)
            tSeen[t[i]] = 1 + tSeen.get(t[i], 0)

        return sSeen == tSeen