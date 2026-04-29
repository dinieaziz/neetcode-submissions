class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        """
        Track each element in list using a hashmap.
        If element already exist, return True. Else, False.
        """

        seen = set()

        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        
        return False