class Solution(object):
    def solveSudoku(self, board):
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        empty = []

        # initialize
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    empty.append((i, j))
                else:
                    c = board[i][j]
                    rows[i].add(c)
                    cols[j].add(c)
                    boxes[(i//3)*3 + (j//3)].add(c)

        def solve(idx):
            if idx == len(empty):
                return True

            i, j = empty[idx]
            box_id = (i//3)*3 + (j//3)

            for c in '123456789':
                if c not in rows[i] and c not in cols[j] and c not in boxes[box_id]:
                    
                    board[i][j] = c
                    rows[i].add(c)
                    cols[j].add(c)
                    boxes[box_id].add(c)

                    if solve(idx + 1):
                        return True

                    # backtrack
                    board[i][j] = '.'
                    rows[i].remove(c)
                    cols[j].remove(c)
                    boxes[box_id].remove(c)

            return False

        solve(0)

        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        