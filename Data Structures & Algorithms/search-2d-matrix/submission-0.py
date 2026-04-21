class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool: 
        n = len(matrix[0])
        m = len(matrix)
        start = n * 0 + 0
        end = n * (m-1) + (n-1)
        i = j = 0
        
        while(start<=end):
            mid = start + (end - start)//2
            i = mid // n
            j = mid - (n*i)
            midij = matrix[i][j]
            # mid = conversion from index length to (i,j)
            if target == midij:
                return True
            
            elif target < midij:
                end = mid - 1
                # end = mid - 1(conversion)
            
            else:
                start = mid + 1
                # start = mid + 1(conversion)
        
        return False