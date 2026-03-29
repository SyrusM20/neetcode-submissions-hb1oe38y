# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        pos = {v : i for i, v in enumerate(inorder)}

        pre_idx = 0
        def build(L, R):
            nonlocal pre_idx

            if L > R:
                return None
            
            root_val = preorder[pre_idx]
            pre_idx += 1

            root = TreeNode(root_val)
            i = pos[root_val]

            root.left = build(L, i - 1)
            root.right = build(i + 1, R)
            return root
        return build(0, len(inorder) - 1)