class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        sudoku_sub_boards: list[tuple[int, int]] = [(0, 2), (3, 5), (6, 8)]

        # check valid row
        for row in board:
            hashmap: dict[str, int] = {}
            for col in row:
                if col == ".":
                    continue

                if int(col) < 1 or int(col) > 9 or col in hashmap:
                    return False
                hashmap[col] = 1

        # check valid col
        for col_idx in range(9):
            hashmap: dict[str, int] = {}
            for row_idx in range(9):
                val = board[row_idx][col_idx]

                if val == ".":
                    continue

                if int(val) < 1 or int(val) > 9 or val in hashmap:
                    return False
                hashmap[val] = 1

        # check valid sub_board
        for sub_board_row in sudoku_sub_boards:
            for sub_board_col in sudoku_sub_boards:
                row_start, row_end = sub_board_row
                col_start, col_end = sub_board_col

                hashmap: dict[str, int] = {}
                for row_idx in range(row_start, row_end + 1):
                    for col_idx in range(col_start, col_end + 1):
                        val = board[row_idx][col_idx]

                        if val == ".":
                            continue

                        if int(val) < 1 or int(val) > 9 or val in hashmap:
                            return False
                        hashmap[val] = 1

        return True


solution = Solution()
first = solution.isValidSudoku([["5", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."], [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"], ["4", ".", ".", "8", ".", "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"], [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"], [".", ".", ".", ".", "8", ".", ".", "7", "9"]])  # ? true
# should be True
print('first: ', first)

# should be False
second = solution.isValidSudoku([["8", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."], [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"], ["4", ".", ".", "8", ".", "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"], [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"], [".", ".", ".", ".", "8", ".", ".", "7", "9"]])  # ? false
print('second: ', second)
