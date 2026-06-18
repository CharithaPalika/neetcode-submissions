class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Row, col check
        for i in range(len(board)):
            row = board[i]
            nums_row = [int(row[i]) for i in range(len(row)) if row[i] != "."]
            if self.is_duplicate(nums_row):
                return False

            col = [r[i] for r in board]
            print(col)
            nums_col = [int(col[i]) for i in range(len(col)) if col[i] != "."]
            if self.is_duplicate(nums_col):
                return False
           
        # 3x3 box checks
        initial_idx = [0, 3, 6]
        final_idx = [2, 5, 8]
        idxs = [(0,3), (3,6), (6,9)]

        for i in range(len(idxs)):
            row_idx = idxs[i]
            for j in range(len(idxs)):
                col_idx = idxs[j]
                box = [board[k][l] for k in range(row_idx[0], row_idx[1]) for l in range(col_idx[0], col_idx[1])] 
                nums_box=[int(box[i]) for i in range(len(box)) if box[i] != "."]
                if self.is_duplicate(nums_box):
                    return False
        return True
        
    def is_duplicate(self, nums):
        seen = set()
        for i in range(len(nums)):
            if nums[i] in seen:
                return True
            seen.add(nums[i])
        return False

        