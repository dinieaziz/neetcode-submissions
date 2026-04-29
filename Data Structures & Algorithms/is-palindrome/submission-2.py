class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        We need to track L and R - 2 pointer
        Check if it is alphanumeric, else skip spaces - isalnum()
        Convert all alphanumeric to same format - lower()

        time:  0(n)
        space: 0(1)
        """

        L = 0
        R = len(s) - 1

        # Loop as long as string is still valid
        while L < R:
            # Shift pointer L/R as long as char is still not alphanumerical
            while L < R and s[L].isalnum() == False:
                L += 1
            while R > L and s[R].isalnum() == False:
                R -= 1

            # If char not same alphanumeric, not a palindrome
            if s[L].lower() != s[R].lower():
                return False

            # Shift to next char
            L += 1
            R -= 1

        return True