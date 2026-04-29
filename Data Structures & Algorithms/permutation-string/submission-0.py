class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
        Sliding window
        
        Time:   0(n)
        Space:  0(1)
        """
    
        # If s1 is longer, there is no way to match
        if len(s1) > len(s2):
            return False

        s1Freq, s2Freq = [0] * 26, [0] * 26

        # Track s1 char frequency, first N value of s2 can be tracked too
        for i in range(len(s1)):
            s1Freq[ord(s1[i]) - ord('a')] += 1
            s2Freq[ord(s2[i]) - ord('a')] += 1

        # Compare the frequency to check initial match count
        matches = 0
        for i in range(26):
            matches += (1 if s1Freq[i] == s2Freq[i] else 0)

        left = 0
        # Start at the index we stopped above initially
        for right in range(len(s1), len(s2)):
            if matches == 26:
                return True
            
            # Check right side, get index to increment in the frequency array
            index = ord(s2[right]) - ord('a')
            s2Freq[index] += 1
            if s1Freq[index] == s2Freq[index]:
                matches += 1
            elif s1Freq[index] + 1 == s2Freq[index]:
                matches -= 1

            # Check left side, get index to increment in the frequency array
            index = ord(s2[left]) - ord('a')
            s2Freq[index] -= 1
            if s1Freq[index] == s2Freq[index]:
                matches += 1
            elif s1Freq[index] - 1 == s2Freq[index]:
                matches -= 1
            
            # Always move left pointer to keep same size window
            left += 1
        return matches == 26

    