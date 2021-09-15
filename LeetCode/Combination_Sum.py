# 解説
# https://leetcode.com/problems/combination-sum/discuss/937255/Python-3-or-DFSBacktracking-and-Two-DP-methods-or-Explanations

class Solution:
    def combinationSum(self, candidates, target):
        ans = []
        n = len(candidates)
        def dfs(cur, cur_sum, idx):# try out each possible cases

            if cur_sum > target:
                return         # this is the case, cur_sum will never equal to target
            if cur_sum == target:
                ans.append(cur); return # if equal, add to `ans`
            for i in range(idx, n):
                dfs(cur + [candidates[i]], cur_sum + candidates[i], i) # DFS

        dfs([], 0, 0)
        return ans

Solve = Solution()
candidates = [2,3,4,7]
target = 8
print(Solve.combinationSum(candidates,target))