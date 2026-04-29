class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        O(n^2) - 2 pointers with 1 fixed digit

        Can traverse string digit twice. Sort by ascending order first.
        Keep 1st digit then 2 pointers extreme left and right.
        If any of the i or pointers are duplicate digit as previous, skip it.

          i L         R
        [-1,0,1,2,-1,-4]
        """
        
        result = []
        nums.sort()

        for i in range(len(nums) - 2):
            left = i + 1
            right = len(nums) - 1

            # Skip duplicate i
            if i > 0 and nums[i] == nums[i - 1]:
                continue  
            
            while left < right:
                if nums[i] + nums[left] + nums[right] == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1

                    # Skip duplicate left
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

                    # Skip duplicate right
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

                elif nums[i] + nums[left] + nums[right] > 0:
                    right -= 1

                else:
                    left += 1
                
        return result
