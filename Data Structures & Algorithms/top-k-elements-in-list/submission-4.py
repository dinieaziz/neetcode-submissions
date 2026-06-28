class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}

        for i in range(len(nums)):
            freq[nums[i]] = 1 + freq.get(nums[i], 0)

        groupedLists = [[] for _ in range(len(nums) + 1)]
        for element, freq in freq.items():
            groupedLists[freq].append(element)

        result = []
        for i in range(len(groupedLists) - 1, 0, -1):
            for res in groupedLists[i]:
                result.append(res)
                if len(result) == k:
                    return result