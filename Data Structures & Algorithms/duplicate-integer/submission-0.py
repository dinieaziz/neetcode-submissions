class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        """
        O(n) - traverse entire array

        Keep track of values tracked. One way is using hashmap.
        Once there is duplicate, return True.
        """

        seen = set()

        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        
        return False

