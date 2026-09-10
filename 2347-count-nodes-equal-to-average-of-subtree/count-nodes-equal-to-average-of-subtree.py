class Solution(object):
    def averageOfSubtree(self, root):

        self.ans = 0

        def dfs(node):

            if node is None:
                return 0, 0

            leftSum, leftCount = dfs(node.left)
            rightSum, rightCount = dfs(node.right)

            totalSum = node.val + leftSum + rightSum
            totalCount = 1 + leftCount + rightCount

            if node.val == totalSum // totalCount:
                self.ans += 1

            return totalSum, totalCount

        dfs(root)

        return self.ans