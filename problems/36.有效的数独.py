# https://leetcode.cn/problems/valid-sudoku/description/
# 请你判断一个 9 x 9 的数独是否有效。只需要 根据以下规则 ，验证已经填入的数字是否有效即可。

#     数字 1-9 在每一行只能出现一次。
#     数字 1-9 在每一列只能出现一次。
#     数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。（请参考示例图）

 

# 注意：

#     一个有效的数独（部分已被填充）不一定是可解的。
#     只需要根据以上规则，验证已经填入的数字是否有效即可。
#     空白格用 '.' 表示。
# 输入：board = 
# [["5","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]
# 输出：true
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        hash
        https://leetcode.cn/problems/valid-sudoku/solutions/1001859/you-xiao-de-shu-du-by-leetcode-solution-50m6/
        """
        lookup_row, lookup_col, lookup_block = ({i:[0]*9 for i in range(9)},
                                                {i:[0]*9 for i in range(9)},
                                                {i:[0]*9 for i in range(9)})
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == ".": continue
                board[i][j] = int(board[i][j])
                lookup_row[i][board[i][j]-1] += 1
                if lookup_row[i][board[i][j]-1]>1:
                    return False
                lookup_col[j][board[i][j]-1] += 1
                if lookup_col[j][board[i][j]-1]>1:
                    return False
                block_ix = i//3 * 3 + j//3
                lookup_block[block_ix][board[i][j]-1] += 1
                if lookup_block[block_ix][board[i][j]-1] > 1:
                    return False
        return True
    def isValidSudoku1(self, board: List[List[str]]) -> bool:
        """暴力解法"""
        def check(i, j):
            # check line
            for jx in range(len(board[i])):
                if jx != j:
                    if board[i][jx] == board[i][j]:
                        return False
            # check col
            for ix in range(len(board)):
                if ix != i:
                    if board[ix][j] == board[i][j]:
                        return False
            # check block
            block_ix, block_jx = i//3, j//3
            for ix in range(3):
                for jx in range(3):
                    ix_ = ix + block_ix*3
                    jx_ = jx + block_jx*3
                    if ix_ == i and jx_==j:
                        continue
                    if board[ix_][jx_] == board[i][j]:
                        return False
            return True

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == '.': continue
                if check(i, j):
                    continue
                return False
        return True