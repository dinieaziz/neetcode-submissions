class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        O(n) - traverse the list but no nested

        Track the number occurence in a dictionary.
        Return the top K occurence of the dictionary.
        Can utilise bucket sort.
        """

        # Count how many times each number appears
        freq = {}
        for num in nums:
            freq[num] = 1 + freq.get(num, 0)

        # Group elements by frequency using bucket
        buckets = [[] for _ in range(len(nums) + 1)]
        for num, count in freq.items():
            buckets[count].append(num)

        # Find the top K element
        result = []
        for i in range(len(buckets)-1, 0, -1):
            for num in buckets[i]:
                result.append(num)
                if len(result) == k:
                    return result
