class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        st = 0
        end = m-1
        lst = []
        while st <=end:
            mid = (st+end)//2
            if matrix[mid][0] <= target and matrix[mid][n-1] >= target:
                lst = matrix[mid]
                break
            elif matrix[mid][n-1] < target:
                st = mid+1
            else:
                end = mid-1
        if not lst:
            return False
        start = 0
        end1 = n-1
        while start<=end1:
            mid = (start+end1)//2
            if lst[mid] == target:
                return True
            elif lst[mid] < target:
                start = mid+1
            else:
                end1 = mid-1
        return False


        