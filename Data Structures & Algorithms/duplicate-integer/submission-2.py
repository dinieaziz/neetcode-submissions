class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        """
        We need to track occurrence of each element in num - hashmap (set)
        If element already in hashmap, return True

        time:  O(n)
        space: O(n)
        """

        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        
        return False
