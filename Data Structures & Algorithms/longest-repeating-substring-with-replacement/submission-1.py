class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        We should always change K amount of characters to follow the most appeared character.
        (Window legth - Most appeared character) <= K.
        
        We can use hashmap to track the most occurred character.
        """

        freq = {}
        result = 0 

        left = 0
        for right in range(len(s)):
            freq[s[right]] = 1 + freq.get(s[right], 0)
            
            while (right - left + 1) - max(freq.values()) > k:
                freq[s[left]] -= 1
                left += 1
            
            result = max(result, right - left + 1)
        return result