class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        We need to track the first element of the pair - hashmap (dict)
        We need to traverse through each element and find its complement - for loop

        time:  0(n)
        space: 0(n)
        """

        seen = {}
        for i, num in enumerate(nums):
            complement = target - nums[i]

            if complement in seen:
                return [seen[complement], i]

            # seen[i] = num # This does not allow looking up for complement as it stores index
            seen[num] = i

        