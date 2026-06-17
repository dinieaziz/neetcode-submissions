class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        
        while l < r:
            m = (l + r) // 2    # l + ((r - l) // 2)

            # Force to start at even index, true if its odd
            if m % 2 == 1:
                m -= 1
            
            # Check if even index is same as odd index,
            # if same means the non-duplicate is on right side
            if nums[m] == nums[m + 1]:
                l = m + 2
            else:
                r = m

        # l or r does not matter as both pointers
        # will end up in the same position
        return nums[r]