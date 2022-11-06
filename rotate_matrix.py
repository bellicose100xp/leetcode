class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        l = len(matrix)

        swapped: dict[str, int] = {}
        original_matrix_val: int = 0

        for ri, rv in enumerate(matrix): # ri = row_index, rv = row_value
            for ci, cv in enumerate(rv): # ci = col_index, cv = col_value
                if swapped.get(f"{ri},{ci}", None) == None:
                    original_matrix_val = cv
                else:
                    original_matrix_val = swapped[f"{ri},{ci}"]

                swapped[f"{ci},{l-1-ri}"] = matrix[ci][l-1-ri]
                matrix[ci][l-1-ri] = original_matrix_val
        
        print(matrix)


solution = Solution()
solution.rotate([[1, 2, 3], [4, 5, 6], [7, 8, 9]])  # [[7,4,1],[8,5,2],[9,6,3]]
solution.rotate([[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]])  # [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
