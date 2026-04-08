# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            if node is None:
                return 0
            
            L = dfs(node.left)
            R = dfs(node.right)

            if L == -1 or R == -1 or abs(L - R) > 1:
                return -1
            
            return max(L, R) + 1 
        return dfs(root) != -1