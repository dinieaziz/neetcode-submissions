class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}

        for i in range(len(nums)):
            freq[nums[i]] = 1 + freq.get(nums[i], 0)
        
        groupedList = [[] for _ in range(len(nums) + 1)]
        for key, value in freq.items():
            groupedList[value].append(key)

        result = []
        for j in range(len(groupedList) - 1, 0 , -1):
            for res in groupedList[j]:
                result.append(res)

                if len(result) == k:
                    return result