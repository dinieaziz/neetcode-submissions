class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        O(n + m) - traverse through each list once

        Both strings must be same size.
        Count the frequency of each character. We can use dictionary for this.
        Return True if both dictionaries are equal
        """

        if len(s) != len(t):
            return False

        countS, countT = {}, {}

        for i in range(len(s)):
            # 1 + current count of character in the dictionary else default 0
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)

        return countS == countT