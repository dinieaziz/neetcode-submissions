class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}
        left, result = 0, 0

        for right in range(len(s)):
            freq[s[right]] = 1 + freq.get(s[right], 0)

            while (right - left + 1) - max(freq.values()) > k:
                freq[s[left]] -= 1
                left += 1
                
            result = max(result, right - left + 1)

        return result