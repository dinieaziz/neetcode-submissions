class Solution:
    def maxArea(self, heights: List[int]) -> int:
        """
        (right - left) * min(height[left], height[right])

        Track the highest water level. Track left and right.
        Replace water level if it is higher.
        Traverse left or right depending on which is a lower height. 
        We always want the highest height.
        """

        left = 0
        right = len(heights) - 1
        maxWaterAmt = 0

        while left < right:
            currentWaterAmt = (right - left) * min(heights[left], heights[right])
            maxWaterAmt = max(maxWaterAmt, currentWaterAmt)
    
            if heights[left] > heights[right]:
                right -= 1
            else:
                left += 1

        return maxWaterAmt
        