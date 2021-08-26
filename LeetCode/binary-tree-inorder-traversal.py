# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.ans = []

    def inorderTraversal(self, root):
        self.dfs(root)
        return self.ans

    def dfs(self, root):
        if root is None:
            return
        self.dfs(root.left)
        self.ans.append(root.val)
        self.dfs(root.right)


ans = Solution()
input = [1,null,2,3]
print(ans.inorderTraversal(input))
