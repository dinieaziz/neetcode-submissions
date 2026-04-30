class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """
        If t is longer than s, return ""
        
        Hashmap to track frequency of characters in t
        
        Initialise have and need hashmap for tracking
        Initialise result array and resultLen value for tracking
        
        Move right pointer and add char into window hashmap
            While have = need, reduce substring till have != need
                If resultLen is shorter, update resultLen
                Shift left pointer till have != need
        
        Return result or ""

        Time:   0(s + t)
        Space:  0(t)
        """
        # If t is longer than s, return ""
        if len(t) > len(s):
            return ""

        # Hashmap to track frequency of characters in t
        tFreq, window = {}, {}
        for char in t:
            tFreq[char] = 1 + tFreq.get(char, 0)

        # Initialise have and need hashmap for tracking
        have, need = 0, len(tFreq)
        
        # Initialise result array and resultLen value for tracking
        result, resultLen = [-1, -1], float("infinity")
        left = 0
        
        # Move right pointer and add char into window hashmap
        for right in range(len(s)):
            char = s[right]
            window[char] = 1 + window.get(char, 0)

            if char in tFreq and window[char] == tFreq[char]:
                have += 1

            # While have = need, reduce substring till have != need
            while have == need:
                # If resultLen is shorter, update resultLen
                if (right - left + 1) < resultLen:
                    result = [left, right]
                    resultLen = (right - left + 1)
                
                # Shift left pointer till have != need
                window[s[left]] -= 1
                if s[left] in tFreq and window[s[left]] < tFreq[s[left]]:
                    have -= 1
                left += 1

        left, right = result
        return s[left : right + 1] if resultLen != float("infinity") else ""