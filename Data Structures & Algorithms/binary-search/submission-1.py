class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        We want a solution in 0(logn) - binary search
        Divide and conquer by splitting into 2 and checking middle

        time:  0(logn)
        space: 0(1)
        """

        left = 0
        right = len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2

            # If mid value is more than target, check left side
            if nums[mid] > target:
                right = mid - 1
            # Elif mid value is less than target, check right side
            elif nums[mid] < target: 
                left = mid + 1
            # Else mid value is equal to target
            else:
                return mid

        return -1

            