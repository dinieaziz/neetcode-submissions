class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        result = [0] * n
        maxNum = -1

        for i in range(n - 1, -1, -1):
            result[i] = maxNum
            maxNum = max(maxNum, arr[i])

        return result

