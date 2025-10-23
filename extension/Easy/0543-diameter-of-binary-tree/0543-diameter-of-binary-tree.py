# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.maxi = 0
        def height(node):
            if not node:
                return 0
            
            lh = height(node.left)
            rh = height(node.right)

            self.maxi = max(self.maxi,lh+rh)

            return max(lh,rh)+1
        height(root)
        return self.maxi

