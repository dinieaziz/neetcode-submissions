class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Create left and right boundary
        # While left is lesser than right
            # Get middle index and value
            # If target found in middle, return
            # If pivot position on right
                # Use binary search, split into halves
            # Else on left
                # Use binary search, split into halves
        # Not found at all, return -1

        left, right = 0, len(nums) - 1

        while left <= right:
            middle = (left + right) // 2

            # Target found
            if nums[middle] == target:
                return middle
            
            # Pivot on right side
            if nums[left] <= nums[middle]:
                # Check if target is on left sorted
                if nums[left] <= target < nums[middle]:
                    right = middle - 1
                # Else is on right sorted
                else:
                    left = middle + 1

            # Pivot on left side
            else:
                # Check if target is on right sorted
                if nums[middle] < target <= nums[right]:
                    left = middle + 1
                # Else is on left sorted
                else:
                    right = middle - 1

        # Cant find
        return -1