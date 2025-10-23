# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxi = float('-inf')
        def maxHt(node):
            nonlocal maxi
            if not node:
                return 0
            lh = max(0, maxHt(node.left))
            rh = max(0, maxHt(node.right))
            maxi = max(maxi, node.val + lh + rh)
            return max(lh,rh) + node.val
        maxHt(root)
        return maxi