class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        nums1Ptr, nums2Ptr = m - 1, n - 1
        posPtr = len(nums1) - 1

        while nums2Ptr >= 0:
            if nums1Ptr >= 0 and nums1[nums1Ptr] > nums2[nums2Ptr]:
                nums1[posPtr] = nums1[nums1Ptr]
                nums1Ptr -= 1
            else:
                nums1[posPtr] = nums2[nums2Ptr]
                nums2Ptr -= 1
            posPtr -= 1
            