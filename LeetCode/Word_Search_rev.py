import sys
sys.setrecursionlimit(10 ** 7)  # 再帰関数の呼び出し制限


class Solution:
    def exist(self, board, word) -> bool:

        if not board:

            # Quick response for empty board
            return False
        # Ｈ行W列を考える
        H,W = len(board), len(board[0])


        def dfs_search(idx,h,w):
            # 場外アウトしたり、移動先が壁の場合はスルー
            if h < 0 or h >= H or w < 0 or w >= W or word[idx] != board[h][w]:
                return False

            # boardの中に一致した文字があった
            if idx == len(word) - 1:
                return True

            cur = board[h][w]

            board[h][w] = "#"

            found = dfs_search(idx+1,h+1,w) or dfs_search(idx+1,h-1,w) or dfs_search(idx+1,h,w+1) or dfs_search(idx+1,h,w-1)

            board[h][w] = cur

            return found

        return any(dfs_search(0,h,w) for w in range(W) for h in range(H))

board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCCED"
Solve = Solution()
print(Solve.exist(board,word))
