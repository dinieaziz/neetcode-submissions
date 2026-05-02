class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
        Initialise result array that will always be length of temperatures
        Use stack to keep track of the temp and index

        Read every value in temperature - enumerate
            while stack is valid and the current temp is warmer, pop out
                Calculate day difference while doing so into result array
            Add the warmer temp and index into stack

        Return result
        

        Time:   O(n)
        Space:  O(n)
        """

        result = [0] * len(temperatures)
        stack = []

        for index, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                stackTemp, stackInd = stack.pop()
                result[stackInd] = index - stackInd
            stack.append((temp, index))
        
        return result