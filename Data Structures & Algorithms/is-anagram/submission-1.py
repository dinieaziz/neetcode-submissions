class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """

        If string size does not match, return False.
        Check occurence of each character. We can use hashmap to count the occurence.
        """

        if len(s) != len(t):
            return False

        countS, countT = {}, {}
        
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        
        return countS == countT

        