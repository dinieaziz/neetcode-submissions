class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        O(n) - Traverse entire list once, sliding window
        Longest unique substring - Sliding window

        Store strings already encountered in hashmap using set.
        Keep track of left, right pointer and the max length found.
        Loop while still within string range.
        Increase left pointer until where duplicate is removed. Repeat loop
        """

        temp = set()
        left = 0
        maxLength = 0

        for right in range(len(s)):
            while s[right] in temp:
                temp.remove(s[left])
                left += 1
            temp.add(s[right])
            maxLength = max (maxLength, right - left + 1)

        return maxLength
