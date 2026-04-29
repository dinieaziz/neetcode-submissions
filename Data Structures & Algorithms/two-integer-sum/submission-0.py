class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        O(n) - traverse list but no nested
        
        There must not be result from the same index.
        Store in a dictionary denoting index and value.

        {[value: index], [value: index]}
        [3,4,5,6] -> {[3: 0], [4: 1], [5: 2]}
        """

        seen = {}
        
        for i, num in enumerate(nums):
            remainder = target - num
            
            if remainder in seen:
                return [seen[remainder], i]
            
            seen[num] = i
