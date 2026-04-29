class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        We need to split the matrix in half every time by row and col - 2 x binary search
            
        time:  0(log (m * n))
        space: 0(1)
        """
        rows, cols = len(matrix), len(matrix[0])

        top = 0  
        bottom = rows - 1
        while top <= bottom:
            mid = (top + bottom) // 2

            # If target is more than the last element, check bottom
            if target > matrix[mid][-1]: 
                top = mid + 1
            # Elif target is less than the first element, check top
            elif target < matrix[mid][0]: 
                bottom = mid - 1
            # Else target is at the correct row
            else:
                break
        
        # Get the middle row that was break at
        row = (top + bottom) // 2

        left = 0
        right = cols - 1
        while left <= right:
            mid = (left + right) // 2

            # If target is bigger than middle element of row, check right
            if target > matrix[row][mid]: 
                left = mid + 1
            # Elif target is lesser than middle element of row, check left
            elif target < matrix[row][mid]:
                right = mid - 1
            # Else target is in middle
            else:
                return True
        return False