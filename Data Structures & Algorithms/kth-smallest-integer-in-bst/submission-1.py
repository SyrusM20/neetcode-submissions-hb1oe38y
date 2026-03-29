# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        seen, ans = 0, None

        def dfs(node):
            nonlocal seen, ans
            if node is None or ans is not None:
                return None
            
            dfs(node.left)
            seen += 1
            if seen == k:
                ans = node.val
                return
            dfs(node.right)

        dfs(root)
        return ans