class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        We need to count each digits occurence. - hashmap
        We need to group the elements by their frequencies. - insert sort
        Finally we get the top K elements.

        [1,2,2,3,3,3,7,7]

        count:
        {1:1}
        {1:1, 2:1}
        {1:1, 2:2}
        {1:1, 2:2, 3:1}
        {1:1, 2:2, 3:2}
        {1:1, 2:2, 3:3, 7:2}

        freq:
        [[], [1], [], [], [], [], []]
        [[], [1], [2], [], [], [], []]
        [[], [1], [2], [3], [], [], []]
        [[], [1], [2,7], [3], [], [], []]
        """

        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)
            # print(count)

        # Size of freq is the max value input num can occur
        freq = [[] for _ in range(len(nums) + 1)]
        for num, count in count.items():
            # print("value", num,  "occurred:", count, "times")
            freq[count].append(num)

        result = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                result.append(num)
                if len(result) == k:
                    return result
