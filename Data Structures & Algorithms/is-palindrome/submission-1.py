class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        Needs to convert string to one case and only detect alphanumeric.
        If detect its not alphanumeric, shift that position +/- 1
        Needs to compare front and back simultaneously. We can use a 2-pointer method.

        L       R
        race car?

                RL    
        No lemon, no melon
        """

        left = 0
        right = len(s) - 1

        # Loop as long as string still valid
        while left < right:
            # Loop as long as it is not a valid character, move pointer accordingly
            while left < right and s[left].isalnum() == False:
                left += 1
            while right > left and s[right].isalnum() == False:
                right -= 1

            # Compare palindrome
            if s[left].lower() != s[right].lower():
                return False
                
            # Update the valid character pointer
            left += 1
            right -= 1
        
        return True