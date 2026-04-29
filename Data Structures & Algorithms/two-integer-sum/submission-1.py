class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """

        Keep track of first digit of pair to check for next pair.
        Can be done by storing in a hashmap since we also need to return the index.
        We do {digit:index} instead of {index:digit} as it allows remainder lookup in O(1) time.

        seen = {digit:index}

         0 1 2 3
        [3,4,5,6]
        """

        seen = {}

        for i, num in enumerate(nums):
            remainder = target - num
            
            if remainder in seen:
                return [seen[remainder], i]

            seen[num] = i