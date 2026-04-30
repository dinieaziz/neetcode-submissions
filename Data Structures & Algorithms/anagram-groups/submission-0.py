class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        Initialise result hashmap to track frequency of strings

        For each string, count the char frequency
            Add char frequency to result hashmap

        Return the grouped hashmap

        Time:   O(m * n) - traverse list and string but not nested
        Space:  O(m) - result hashmap
        """

        # Initialise result hashmap to track frequency of strings
        result = defaultdict(list)

        # For each string, count the char frequency
        for string in strs:
            count = [0] * 26

            for char in string:
                count[ord(char) - ord("a")] += 1

            # Add char frequency to result hashmap
            result[tuple(count)].append(string)

        return list(result.values())