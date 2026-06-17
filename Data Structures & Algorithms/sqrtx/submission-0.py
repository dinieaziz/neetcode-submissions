class Solution:
    def mySqrt(self, x: int) -> int:
        # Babylonian algo

        nx = 1
        for i in range(0, 50, 1):
            n = (nx + x / nx) / 2
            nx = n

        return int(nx)