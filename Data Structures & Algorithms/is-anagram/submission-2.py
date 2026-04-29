class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        If string size is different, is definitely not an anagram - edgecase
        We need to count the occurrence of each alphabet for each string - hashmap (dictionary)

        time:  O(n+m)
        space: O(1)
        """

        if len(s) != len(t):
            return False

        seenS, seenT = {}, {}
        for i in range(len(s)):
            seenS[s[i]] = 1 + seenS.get(s[i], 0)
            seenT[t[i]] = 1 + seenT.get(t[i], 0)

        # if seenS == seenT:
        #     return True
        # else:
        #     return False
        return seenS == seenT