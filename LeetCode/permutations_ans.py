# 天才やdfs
# 解説[再帰関数を用いた深さ優先探索(DFS)による全探索アルゴリズム]("https://algo-logic.info/brute-force-dfs/")

class Solution:
    def permute(self, l):#-> List[List[int]]:
        def dfs(path, used, res):
            if len(path) == len(l):
                res.append(path[:]) # note [:] make a deep copy since otherwise we'd be append the same list over and over
                return

            for i, letter in enumerate(l):
                # skip used letters
                if used[i]:
                    continue
                # add letter to permutation, mark letter as used
                path.append(letter)
                used[i] = True
                dfs(path, used, res)
                # remove letter from permutation, mark letter as unused
                path.pop()
                used[i] = False

        res = []
        dfs([], [False] * len(l), res)
        return res

a = Solution()
num = [1,2,3]
print(a.permute(num))