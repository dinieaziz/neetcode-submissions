class Solution:
    def isValid(self, s: str) -> bool:
        """
        We need to keep track of the opening and closing brackets in sequence - stack

        time:  0(n)
        space: 0(n)
        """

        stack = []
        closingPair = {")":"(", "}":"{", "]":"["}
        
        for bracket in s:
            # If it is a closing bracket, check for matching pair
            if bracket in closingPair:
                # If stack is not empty and is a matching pair
                if stack and stack[-1] == closingPair[bracket]:
                    stack.pop() # Popping list removes the last element if not specified
                else:
                    return False
                    
            # Else, add it to stack
            else:
                stack.append(bracket)
        
        # If stack has remainder, is invalid
        if stack:
            return False
        # Else, is valid
        else:
            return True