class Solution(object):
    def maxDepth(self, root):
        if root is None:
            return 0

        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)

        if left < right:
            return right + 1
        else:
            return left + 1